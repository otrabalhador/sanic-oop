import routes
from app import app


def run():
    routes.start_routes()
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run()
