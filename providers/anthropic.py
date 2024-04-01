import anthropic
from .base_provider import BaseProvider
from exceptions.error import InternalServerError


class AnthropicProvider(BaseProvider):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.client = anthropic.Anthropic(api_key=api_key)

    def complete(self, prompt, max_tokens, temperature, top_p):
        try:
            message = self.client.messages.create(
                model="claude-3-sonnet-20240229",  # there are multiple models provided, based on speed or accuracy
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                top_p=top_p
            )
            return message.content[0].text
        except anthropic.RateLimitError as error:
            raise InternalServerError("Anthropic plan exhausted, we will be back on this.")
        except anthropic.APIConnectionError as error:
            raise InternalServerError("The server could not be reached")
        except Exception as exception:
            raise InternalServerError(exception)
