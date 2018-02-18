from sanic import exceptions

from error_handler.custom_error_handler import CustomErrorHandler


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


class Error404Handler(CustomErrorHandler):
    def __init__(self):
        self.response = Error404Response()
        self.exception = exceptions.NotFound
        super().__init__(self.exception,
                         self.response.html_str,
                         self.response.status_code,
                         self.response.headers)
