import os

import middlewares
import routes
from app import app
from listeners import ListenerSetup, ListenerCollection


def setup(sanic_app):
    routes.start_routes()
    middlewares.MiddlewareSetup(sanic_app, middlewares.middleware_objects).setup_middlewares()

    listeners = ListenerCollection().listeners
    ListenerSetup(sanic_app, listeners).setup_listeners()


def get_config_variables() -> dict:
    host = "0.0.0.0"
    port = 8000
    debug = True if os.getenv("DEBUG", False) else False
    return {
        "host": host,
        "port": port,
        "debug": debug
    }


def run():
    setup(app)
    configuration = get_config_variables()
    app.run(**configuration)


if __name__ == "__main__":
    run()
