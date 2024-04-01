

class InternalServerError(Exception):
    """Error to be raised when there is failure from downstream service/API call or server failure.
    """

    def __init__(self, message):
        self.message = message
