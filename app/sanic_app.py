from sanic import Sanic

from app.setup import SanicAppSetup
from api.common.error_handler import ErrorHandlerCollection


class _SanicApp:
    """
        This is a private class for initialization of
        Sanic web server. It is called only once for each runtime,
        when this module is imported.
        You should not initialize this class. Use app variable to
        reference the sanic app.
    """

    def __init__(self):
        self.__app = self._init_app()
        self._setup_app()

    def _init_app(self):
        app_config = self._get_app_configuration()
        sanic_app = Sanic(**app_config)
        return sanic_app

    @staticmethod
    def _get_app_configuration() -> dict:
        return {
            "error_handler": ErrorHandlerCollection()
        }

    def _setup_app(self):
        SanicAppSetup(self.__app).setup()

    @property
    def app(self):
        return self.__app


app = _SanicApp().app
