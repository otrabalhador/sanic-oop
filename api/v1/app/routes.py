from api.v1.controllers.basic import BasicResources
from api.v1.controllers.stream import StreamResource

version = "v1"


def start_routes(app):
    """
       Start application routes
    :return:
    """
    # Basic
    basic_resources = BasicResources(app)
    app.add_route(basic_resources.index, "/", version=version)
    app.add_route(basic_resources.redirect_url, "/redirect", strict_slashes=True, version=version)
    app.add_route(basic_resources.post_handler, "/posts/<post_id>", name="post", version=version)
    app.add_route(basic_resources.internal_server_error, "/error", version=version)

    # Streaming
    stream_resource = StreamResource(app)
    app.add_route(stream_resource.stream, "/stream", version=version)
    app.add_route(stream_resource.stream_from_file, "/stream_from_file", version=version)

    # Static
    app.static("/static", "./static")
