from sanic.response import redirect, text, json

from app import app


async def index(request):
    return json(
        {
            "hello": "world"
        }
    )


async def redirect_url(request):
    url = app.url_for("post", post_id=5, arg=123, arg_2=[12312312, 12312])
    return redirect(url)


async def post_handler(request, post_id):
    return text('Post - {}'.format(post_id))


async def internal_server_error(request):
    division_by_zero = 1 / 0
    return text("ok")
