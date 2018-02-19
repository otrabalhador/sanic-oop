from sanic import exceptions

from error_handler.custom_error_handler import CustomErrorHandler


class ServerErrorResponse:
    def __init__(self):
        self.status_code = 500
        self.headers = None
        self.html_str = """
<body style="background-color: yellow;">
    <h1>Fuck maaaaan</h1>
    <h2>Something awful happened</h2>
    <p>Sorry, mate!!</p>
</body>
"""


class ServerErrorHander(CustomErrorHandler):
    def __init__(self):
        self.response = ServerErrorResponse()
        self.exception = exceptions.ServerError
        super().__init__(self.exception,
                         self.response.html_str,
                         self.response.status_code,
                         self.response.headers)
