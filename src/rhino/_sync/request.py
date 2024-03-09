class Request:
    """
    Holds information about an HTTP request.
    """

    def __init__(self, environ):
        self.environ = environ

    @property
    def method(self) -> str:
        """
        The HTTP request method.
        """
        return self.environ["REQUEST_METHOD"]

    @property
    def path(self) -> str:
        """
        The request path.
        """
        return self.environ["PATH_INFO"]
