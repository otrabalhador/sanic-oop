from app import app
from config import get_config_variables
from setup import AppSetup


def run():
    configuration = get_config_variables()
    app.setup(AppSetup)
    app.run(**configuration)


if __name__ == "__main__":
    run()
