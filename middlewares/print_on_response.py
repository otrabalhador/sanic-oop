from middlewares.api_middleware import SanicMiddleware


class PrintOnResponseMiddleware(SanicMiddleware):
    def __init__(self):
        attach_to = "response"
        middleware = self._print_on_response
        super().__init__(middleware, attach_to)

    @staticmethod
    async def _print_on_response(request, response):
        print("I print when a response is returned by the server")
