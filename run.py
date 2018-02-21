import os

from app import app


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
    configuration = get_config_variables()
    app.run(**configuration)


if __name__ == "__main__":
    run()
