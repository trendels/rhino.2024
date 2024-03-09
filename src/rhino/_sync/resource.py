from ..response import Response
from .context import Context
from .types import Handler


class Resource:
    def __init__(self):
        self._handlers: dict[str, Handler] = {}

    def _add_handler(self, method: str, handler: Handler) -> None:
        self._handlers[method] = handler

    def _handle_request(self, ctx: Context) -> Response:
        request_method = ctx.request.method
        return self._handlers[request_method](ctx)
