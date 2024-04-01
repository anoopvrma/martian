import together

from .base_provider import BaseProvider
from exceptions.error import InternalServerError


class TogetherProvider(BaseProvider):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.api_key = api_key

    def complete(self, prompt, max_tokens, temperature, top_p, stream):
        try:
            together.api_key = self.api_key
            response = together.Complete.create(
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
            )
            return response['output']['choices'][0]['text']
        except together.RateLimitError as error:
            raise InternalServerError("Together AI plan exhausted, we will be back on this.")
        except together.TogetherException as error:
            raise InternalServerError("The server could not be reached")
        except Exception as exception:
            raise InternalServerError(exception)