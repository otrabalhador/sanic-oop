from app import app
from resources.resources import (
    index,
    redirect_url,
    post_handler
)

version = "v1"


def start_routes():
    app.add_route(index, "/", version=version)
    app.add_route(redirect_url, "/redirect", strict_slashes=True, version=version)
    app.add_route(post_handler, "/posts/<post_id>", name="post", version=version)
