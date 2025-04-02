import json
import logging
import os
import re
import time
from typing import List, Dict, Any

import requests
import yaml


class PromptProcessor:
    FILE_PLACEHOLDER = "###FILE:<filename>###```<content>````"
    OUTPUT_FILE_REGEXP = r'###FILE:(.*?)###\s*```(?:\w+)?\s*(.*?)```'
    TOGETHER_API_URL = os.getenv('TOGETHER_API_URL', 'https://api.together.xyz/v1/chat/completions')

    def __init__(self, default_model_config: dict):
        self.logger = self._setup_logging()
        self.api_key = os.getenv('TOGETHER_API_KEY')
        if not self.api_key:
            raise ValueError("TOGETHER_API_KEY environment variable is required")

        self.default_model_config = default_model_config or {
            "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
            "messages": [],
            "max_tokens": None,
            "temperature": 0.7,
            "top_p": 0.7,
            "top_k": 50,
            "repetition_penalty": 1,
            "stop": [
                "<｜end▁of▁sentence｜>"
            ],
            "stream": False
        }

    def _setup_logging(self) -> logging.Logger:
        """Configure and return a logger instance."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger(self.__class__.__name__)

    def _log_non_scalar(self, data: Any, context: str = "") -> None:
        """Log non-scalar values as JSON."""
        if isinstance(data, (dict, list, tuple)):
            self.logger.info(f"{context}: {json.dumps(data, indent=2)}")

    def process_prompts(self, yaml_data) -> list[Dict[str, str]]:
        self.logger.info(f"Starting process_prompts with file")

        result = []

        try:
            for prompt in yaml_data:
                prompt_result = self._process_prompt(prompt)
                result.append(prompt_result)

        except Exception as e:
            self.logger.error(f"Error processing prompts: {str(e)}")
            raise
        
        return result

    @staticmethod
    def _load_yaml_file(file_path: str) -> List[Dict[str, Any]]:
        """Load and parse YAML file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def _process_prompt(self, prompt: Dict[str, Any]) -> Dict[str, str]:
        self.logger.info(f"Processing prompt: {prompt.get('prompt', '')[:50]}...")
        self._log_non_scalar(prompt, "Prompt")

        processed_prompt = self._prepare_prompt(prompt)

        payload = self._prepare_request_payload(prompt, processed_prompt)
        self._log_non_scalar(payload, "Request payload")

        response = self._make_api_call(payload)

        result = self._process_ai_response(response)

        return result

    def _prepare_prompt(self, prompt_obj: Dict[str, Any]) -> str:
        """Prepare the prompt by replacing placeholders."""
        prompt = prompt_obj['prompt']

        if 'outputFiles' in prompt_obj:
            # Filter out excluded files
            included_files = [
                f for f in prompt_obj['outputFiles']
                if not f.get('exclude', False)
            ]

            if included_files:
                files_json = json.dumps(included_files, indent=2)
                prompt = prompt.replace('###OUTPUT_FILES###', files_json)

        # Append file generation instructions
        prompt += f"\n\nOutput files must use this format: {self.FILE_PLACEHOLDER}"
        return prompt

    def _prepare_request_payload(self, prompt_obj: Dict[str, Any], processed_prompt: str) -> Dict[str, Any]:
        """Prepare the request payload for the API call."""
        # Start with default config
        payload = self.default_model_config.copy()

        # Add the current prompt as a user message
        if 'messages' not in payload:
            payload['messages'] = []

        payload['messages'].append({
            "role": "user",
            "content": processed_prompt
        })

        if 'model' in prompt_obj:
            payload.update(prompt_obj['model'])

        return payload

    def _make_api_call(self, payload: Dict[str, Any], retry_count: int = 0) -> Dict[str, Any]:
        """Make the API call with retry logic."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(
                self.TOGETHER_API_URL,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 429:
                if retry_count < 3:
                    wait_time = 10 * (retry_count + 1)
                    self.logger.info(f"Rate limited. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                    return self._make_api_call(payload, retry_count + 1)
                else:
                    raise Exception("Max retries exceeded for rate limiting")

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            self.logger.error(f"API call failed: {str(e)}")
            raise

    def _process_ai_response(self, response: Dict[str, Any]) -> Dict[str, str]:
        """Process the AI response and extract files."""
        self._log_non_scalar(response, "AI Response")

        if 'choices' not in response or not response['choices']:
            self.logger.warning("No choices in AI response")
            
            return {}

        content = response['choices'][0].get('message', {}).get('content', '')
        if not content:
            self.logger.warning("No content in AI response")
            return {}

        files = self._extract_files_from_content(content)

        return files
    
    def _extract_files_from_content(self, content: str) -> Dict[str, str]:
        matches = re.finditer(self.OUTPUT_FILE_REGEXP, content, re.DOTALL)

        files = {match.group(1).strip(): match.group(2).strip() for match in matches }

        return files
