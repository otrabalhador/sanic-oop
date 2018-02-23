from sanic_oop.middlewares.api_middleware import SanicMiddleware


class OnRequestMiddleware(SanicMiddleware):
    """
        Use this to intercept request. You may want to:
        i) check and do something
            For example, you can throw an exception if some attribute of
            request is invalid
        ii) alter request:
            You can change any attribute of sanic request.
        iii) respond early:
            You can do this by returning a sanic.response object on middleware classmethod

        Check the implementation:
            - request object: sanic.request.Request
    """
    attach_to = "request"

    def __init__(self, middleware: classmethod):
        super().__init__(middleware, self.attach_to)

    @staticmethod
    async def _act_on_request(request):
        print("I print when a request is received by the server")
