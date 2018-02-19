from middlewares.api_middleware import SanicMiddleware


class PrintOnRequestMiddleware(SanicMiddleware):
    def __init__(self):
        attach_to = "request"
        middleware = self._print_on_request
        super().__init__(middleware, attach_to)

    @staticmethod
    async def _print_on_request(request):
        print("I print when a request is received by the server")
