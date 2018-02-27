from sanic_oop.middlewares.on_response import OnResponseMiddleware


class SniffResponse(OnResponseMiddleware):
    def __init__(self):
        middleware = self._sniff_response
        super().__init__(middleware=middleware)

    @staticmethod
    def _sniff_response(request, response):
        print("Returning status code %d" % response.status)
