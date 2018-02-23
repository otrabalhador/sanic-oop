from api.common.middlewares.path_required import ForbiddenQueryString
from api.common.middlewares.sniff_response import SniffResponse

middleware_objects = [ForbiddenQueryString, SniffResponse]
