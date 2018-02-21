from routes import v1 as current_version


def start_routes(app):
    current_version.start_routes(app)
