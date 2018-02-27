from sanic import exceptions

from sanic_oop.error_handler.custom_error_handler import CustomErrorHandler


class Error404Response:
    def __init__(self):
        self.status_code = 404
        self.headers = None
        self.html_str = """
<body>
    <div style="height:100vh;position:relative;top:0;left:0;background-color:black;padding:0;margin:0;border:0;">
        <iframe src="https://giphy.com/embed/l1J9EdzfOSgfyueLm" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen>
        </iframe>
    </div>
</body>
"""


class Error404Handler(CustomErrorHandler):
    def __init__(self):
        response = Error404Response()
        super().__init__(exceptions=[exceptions.NotFound],
                         html_str=response.html_str,
                         status_code=response.status_code,
                         headers=response.headers)
