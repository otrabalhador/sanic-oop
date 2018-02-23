from sanic.exceptions import InvalidUsage

from sanic_oop.middlewares.on_request import OnRequestMiddleware


class ForbiddenQueryString(OnRequestMiddleware):
    def __init__(self):
        middleware = self._forbidden_query_string
        super().__init__(middleware=middleware)

    @staticmethod
    def _forbidden_query_string(request):
        if request.args != {}:
            raise InvalidUsage("Query string are forbidden. User has passed %r" % request.args)
