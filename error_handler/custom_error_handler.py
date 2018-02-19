from sanic import response
from sanic.handlers import ErrorHandler


class CustomErrorHandler(ErrorHandler):
    def __init__(self, exceptions, html_str, status_code, headers):
        self.exceptions = exceptions
        self.html_str = html_str
        self.status_code = status_code
        self.headers = headers
        super().__init__()

    def handler(self, request, exception) -> response.html:
        self.log("""\
Handling exception: %r
for request url: %s\
""" % (exception, request.url))
        return response.html(self.html_str,
                             self.status_code,
                             self.headers)

    def get_error_handlers(self) -> list:
        if isinstance(self.exceptions, list):
            return [(exception, self.handler,) for exception in self.exceptions]
        return [(self.exceptions, self.handler,)]
