
class BaseProvider:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def complete(self, prompt: str, max_tokens: int, temperature: float, top_p: float, stream: bool):
        """
        Abstract method to be implemented by subclasses.
        """
        raise NotImplementedError("complete method must be implemented by subclasses")
