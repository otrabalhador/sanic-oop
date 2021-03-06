from sanic_oop.middlewares.api_middleware import SanicOOPMiddleware


class OnResponseMiddleware(SanicOOPMiddleware):
    """
        Use this to intercept after processing of request (before returning response to user).
        You may want to:
        i) check request:
            For example, you can throw an exception if some attribute of
            request is invalid
        ii) check response:
            For example, you can throw an exception if some attribute of
            response is invalid
        iii) alter response:
            You can change any attribute of sanic's response.
        iv) respond early:
            You can do this by returning a sanic.response object on middleware classmethod
            Why does this matter on a middleware response interceptor?
            I don't know. But this feature is available!
        * you can also alter request, but it will be inefficient, since the request was already processed


        Check the implementation:
            - request object: sanic.request.Request
            - response object: sanic.response.BaseHTTPResponse:
                - This object can be either sanic.response.HTTPResponse or StreamingHTTPResponse
    """
    attach_to = "response"

    def __init__(self, middleware: classmethod):
        super().__init__(middleware, self.attach_to)
