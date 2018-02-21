from app import app
from config import get_config_variables


def run():
    configuration = get_config_variables()
    app.run(**configuration)


if __name__ == "__main__":
    run()
