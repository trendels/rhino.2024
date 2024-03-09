from collections.abc import Iterator

import httpx
import pytest

from rhino import Application, Context, Mapper
from rhino.response import Response, ok


@pytest.fixture
def mapper() -> Mapper:
    return Mapper()


@pytest.fixture
def app(mapper: Mapper) -> Application:
    return mapper.make_wsgi_app()


@pytest.fixture
def client(app: Application) -> Iterator[httpx.Client]:
    with httpx.Client(
        transport=httpx.WSGITransport(app=app), base_url="http://test"
    ) as client:
        yield client


def test_returns_404_with_no_handlers(client: httpx.Client):
    """
    An application without handlers responds to all requests with a 404 response.
    """
    response = client.get("/")

    assert response.status_code == 404
    assert response.headers["content-type"] == "text/plain; charset=utf-8"
    assert response.text == "Resource not found."


def test_returns_content_from_handler(mapper: Mapper, client: httpx.Client):
    """
    The application returns content from a handler.
    """

    @mapper.get("/")
    def index(ctx: Context) -> Response:
        return ok("hello, world")

    response = client.get("/")

    assert response.status_code == 200
    assert response.text == "hello, world"


def test_default_content_type_is_text(mapper: Mapper, client: httpx.Client):
    """
    The default content-type for text content is text/plain.
    """

    @mapper.get("/")
    def index(ctx: Context) -> Response:
        return Response(200, None, "hello, world")

    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/plain; charset=utf-8"
