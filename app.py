from sanic import Sanic

from error_handler import ErrorHandlerCollection


class _SanicApp:
    """
        This is a private class for initialization of
        Sanic web server. It is called only once for each runtime.
        You should not initialize this class. Use app variable to
        reference app.
    """
    def __init__(self):
        self.__error_handler = ErrorHandlerCollection()
        self.__app = Sanic(error_handler=ErrorHandlerCollection())

    @property
    def app(self):
        return self.__app


app = _SanicApp().app
