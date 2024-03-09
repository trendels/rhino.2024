from http import HTTPStatus
from typing import Callable

from ..response import Response
from .context import Context
from .request import Request
from .resource import Resource
from .types import Handler


class Mapper:
    """
    Maps URLs to resources.
    """

    def __init__(self):
        self._resources: dict[str, Resource] = {}

    def make_wsgi_app(self) -> "Application":
        """
        Create a WSGI app for this mapper.
        """
        return Application(mapper=self)

    def _handle_request(self, ctx: Context) -> Response:
        try:
            resource = self._resources[ctx.request.path]
        except KeyError:
            return Response(404, None, "Resource not found.")
        return resource._handle_request(ctx)

    def get(self, path: str) -> Callable[[Handler], Handler]:
        """
        Decorator to register a GET handler for `path`.
        """

        def decorator(handler: Handler) -> Handler:
            resource = self._resources.get(path) or Resource()
            resource._add_handler("GET", handler)
            self._resources[path] = resource
            return handler

        return decorator


class Application:
    """
    Provides the WSGI application interface.
    """

    def __init__(self, mapper: Mapper):
        self.mapper = mapper

    def __call__(self, environ, start_response):
        request = Request(environ)
        ctx = Context(request)
        response = self.mapper._handle_request(ctx)
        try:
            reason = HTTPStatus(response.status_code).phrase
        except ValueError:
            reason = "Unknown"
        response.headers.setdefault("content-type", "text/plain; charset=utf-8")
        start_response(
            f"{response.status_code} {reason}", list(response.headers.items())
        )
        if response.content is None:
            return []
        else:
            return [response.content.encode("utf-8")]
