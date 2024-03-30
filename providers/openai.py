import os
from openai import OpenAI

from .base_provider import BaseProvider


class OpenAIProvider(BaseProvider):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.client = OpenAI(api_key=api_key)

    def complete(self, prompt, max_tokens, temperature, top_p):
        # Make a completion request to OpenAI's API
        response = self.client.chat.completions.create(
            messages=[
            {
                "role": "user",
                "content": prompt,
            }
            ],
            model="gpt-3.5-turbo",
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p
        )
        # Extract and return the generated text
        return response
