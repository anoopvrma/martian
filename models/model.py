from providers.openai import OpenAIProvider
from providers.anthropic import AnthropicProvider
from providers.togetherai import TogetherProvider


class Model:
    def __init__(self, provider_name, api_key=None):
        self.provider_name = provider_name
        self.api_key = api_key
        if self.provider_name == 'openai':
            self.provider = OpenAIProvider(api_key)
        elif self.provider_name == 'anthropic':
            self.provider = AnthropicProvider(api_key)
        elif self.provider_name == 'together':
            self.provider = TogetherProvider(api_key)

        # Initialize other provider classes as needed

    def complete(self, prompt, max_tokens, temperature, top_p, stream):
        return self.provider.complete(prompt, max_tokens, temperature, top_p, stream)
        # Implement similar logic for other providers
