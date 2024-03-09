class Response:
    """
    Holds information about an HTTP response.
    """

    status_code: int
    headers: dict[str, str]
    content: str | None

    def __init__(
        self,
        status_code: int,
        headers: dict[str, str] | None = None,
        content: str | None = None,
    ):
        self.status_code = status_code
        self.headers = headers or {}
        self.content = content


def ok(content: str | None) -> Response:
    """
    Creates a "200 OK" response.
    """
    return Response(200, content=content)
