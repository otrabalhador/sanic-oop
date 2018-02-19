from middlewares.setup import SetupMiddlewares
from middlewares.path_required import ForbiddenQueryString
from middlewares.sniff_response import SniffResponse

__all__ = [SetupMiddlewares, ForbiddenQueryString, SniffResponse]

middleware_objects = [ForbiddenQueryString, SniffResponse]
