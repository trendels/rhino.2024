from dataclasses import dataclass

from .request import Request


@dataclass
class Context:
    """
    The request context.
    """

    #: The current request
    request: Request
