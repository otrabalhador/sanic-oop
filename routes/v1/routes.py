from api_resources.basic import (
    index,
    redirect_url,
    post_handler,
    internal_server_error
)
from api_resources.stream import (
    stream,
    stream_from_file
)
from app import app

version = "v1"


def start_routes():
    """
       Start application routes
    :return:
    """
    # Basic
    app.add_route(index, "/", version=version)
    app.add_route(redirect_url, "/redirect", strict_slashes=True, version=version)
    app.add_route(post_handler, "/posts/<post_id>", name="post", version=version)
    app.add_route(internal_server_error, "/error", version=version)

    # Streaming
    app.add_route(stream, "/stream", version=version)
    app.add_route(stream_from_file, "/stream_from_file", version=version)

    # Static
    app.static("/static", "./static")
