from sanic.response import redirect, text, json


class BasicResources:
    def __init__(self, app):
        self.__app = app

    @staticmethod
    async def index(request):
        return json(
            {
                "hello": "world"
            }
        )

    async def redirect_url(self, request):
        url = self.__app.url_for("post", post_id=5, arg=123, arg_2=[12312312, 12312])
        return redirect(url)

    @staticmethod
    async def post_handler(request, post_id):
        return text('Post - {}'.format(post_id))

    @staticmethod
    async def internal_server_error(request):
        division_by_zero = 1 / 0
        return text("ok")
