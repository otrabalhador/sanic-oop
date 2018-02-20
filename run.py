import os

import middlewares
import routes
from app import app


def run():
    debug = True if os.getenv("DEBUG", False) else False
    routes.start_routes()
    middlewares.MiddlewareSetup(app, middlewares.middleware_objects).setup_middlewares()
    app.run(host="0.0.0.0", port=8000, debug=debug)


if __name__ == "__main__":
    run()
