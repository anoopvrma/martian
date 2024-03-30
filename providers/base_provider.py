
class BaseProvider:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def complete(self, prompt, max_tokens, temperature, top_p):
        """
        Abstract method to be implemented by subclasses.
        """
        raise NotImplementedError("complete method must be implemented by subclasses")
