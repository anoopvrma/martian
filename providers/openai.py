import os

import openai
from openai import OpenAI

from .base_provider import BaseProvider
from exceptions.error import InternalServerError


class OpenAIProvider(BaseProvider):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.client = OpenAI(api_key=api_key)

    def complete(self, prompt, max_tokens, temperature, top_p):
        # Make a completion request to OpenAI's API
        try:
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
        except openai.RateLimitError as error:
            raise InternalServerError("OpenAI plan exhausted, we will be back on this.")
        except openai.APIConnectionError as error:
            raise InternalServerError("The server could not be reached")
        except Exception as exception:
            raise InternalServerError(exception)