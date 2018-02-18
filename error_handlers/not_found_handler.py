from sanic.response import html
from sanic import exceptions


class Error404Response:
    def __init__(self):
        self.status_code = 404
        self.headers = None
        self.html_str = """
<body>
    <h1>Yooo, motherfucker!!</h1>
    <h1>404 Error!!</h1>
</body>
"""


class Error404Handler:
    def __init__(self):
        self.exception = exceptions.NotFound
        self.response = Error404Response()

    def handler(self, request, exception):
        return html(self.response.html_str,
                    self.response.status_code,
                    self.response.headers)

    def get_error_handler(self):
        return self.exception, self.handler
