import traceback
import random
from anthropic import Anthropic
from typing import List, Dict, Optional, AsyncGenerator
from descartkit.utils import logger
from descartkit.llm.models import ModelStrategy, LanguageModelProperty


class AnthropicStrategy(ModelStrategy):

    def get_name(self) -> str:
        return "anthropic"

    def base_url(self) -> str | None:
        return None

    def __init__(self, keys: Dict[str, str], model_property: LanguageModelProperty):
        self._keys = keys
        self._property = model_property
        self._client_pool = self._initialize_client_pool()

    def _initialize_client_pool(self) -> List[Dict[str, Anthropic]]:
        return [{"name": k, "client": Anthropic(api_key=v)} for k, v in self._keys.items()]

    def _get_client(self) -> Dict[str, Anthropic]:
        if not self._client_pool:
            raise Exception(f"No {self.get_name()} client available.")
        return random.choice(self._client_pool)

    async def gen_messages(
            self, question: str, system_prompt: Optional[str] = None, history_messages: Optional[List[Dict]] = None
    ) -> List[Dict[str, str]]:
        messages = []
        if system_prompt:
            messages.append({'system': system_prompt})
        if history_messages:
            messages.extend(history_messages)
        if question:
            messages.append({'role': 'user', 'content': question})
        return messages

    async def chat(self, messages: List[Dict[str, str]]) -> str:
        client_info = self._get_client()
        client_name, client = client_info["name"], client_info["client"]

        system_prompt = ""
        new_messages = []
        for one in messages:
            content = one.get("system")
            if content:
                system_prompt = content
            else:
                new_messages.append(one)
        try:
            response = client.messages.create(
                model=self._property.name,
                system=system_prompt,
                messages=new_messages,
                timeout=self._property.timeout,
                temperature=self._property.temperature,
                top_p=self._property.top_p,
                max_tokens=self._property.max_output_token
            )
            return response.content[0].text
        except Exception as e:
            logger.error(
                f"\nContent Generate error: "
                f"\nLLM {self._property.name}@key: {client_name}"
                f"\nError: {traceback.format_exc()}"
            )
            raise e

    async def chat_stream(self, messages: List[Dict[str, str]]) -> AsyncGenerator[str, None]:
        client_info = self._get_client()
        client_name, client = client_info["name"], client_info["client"]

        try:
            for part in client.messages.create(
                model=self._property.name,
                messages=messages,
                timeout=self._property.timeout,
                temperature=self._property.temperature,
                top_p=self._property.top_p,
                max_tokens=self._property.max_output_token,
                stream=True
            ):
                if part.choices:
                    content = part.choices[0].delta.content
                    if content:
                        yield content
        except Exception as e:
            logger.error(
                f"\nContent Generate Stream error: "
                f"\nLLM {self._property.name}@key: {client_name}"
                f"\nError: {traceback.format_exc()}"
            )
            raise e