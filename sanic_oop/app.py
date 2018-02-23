from sanic import Sanic


class SanicOOP(Sanic):
    def __init__(self):
        super().__init__()

    def setup(self, setup_object) -> None:
        setup_instance = setup_object(self)
        setup_instance.setup()
