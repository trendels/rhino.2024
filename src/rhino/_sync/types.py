from typing import Callable, TypeAlias

from ..response import Response
from .context import Context

Handler: TypeAlias = Callable[[Context], Response]
