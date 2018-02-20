from middlewares.setup import MiddlewareSetup
from middlewares.path_required import ForbiddenQueryString
from middlewares.sniff_response import SniffResponse

__all__ = [MiddlewareSetup, ForbiddenQueryString, SniffResponse]

middleware_objects = [ForbiddenQueryString, SniffResponse]
