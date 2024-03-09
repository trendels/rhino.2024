import httpx
from helloworld import app


def test_index():
    with httpx.Client(
        transport=httpx.WSGITransport(app=app), base_url="http://helloworld"
    ) as client:
        response = client.get("/")

    assert response.headers["content-type"] == "text/plain; charset=utf-8"
    assert response.text == "Hello, world!"
