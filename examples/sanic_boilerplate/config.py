import os


def get_config_variables() -> dict:
    host = "0.0.0.0"
    port = 8000
    debug = True if os.getenv("DEBUG", False) else False
    return {
        "host": host,
        "port": port,
        "debug": debug
    }
