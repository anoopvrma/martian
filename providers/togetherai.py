import together

from .base_provider import BaseProvider


class TogetherProvider(BaseProvider):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.api_key = api_key

    def complete(self, prompt, max_tokens, temperature, top_p):
        together.api_key = self.api_key
        response = together.Complete.create(
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p
        )
        return response['output']['choices'][0]['text']
