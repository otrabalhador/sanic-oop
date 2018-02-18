from sanic.handlers import ErrorHandler
from sanic.response import html


class CustomErrorHandler(ErrorHandler):
    def __init__(self, exception, html_str, status_code, headers):
        self.exception = exception
        self.html_str = html_str
        self.status_code = status_code
        self.headers = headers
        super().__init__()

    def handler(self, request, exception):
        self.log("Handling exception: %r " % exception)
        return html(self.html_str,
                    self.status_code,
                    self.headers)

    def get_error_handler(self):
        return self.exception, self.handler
