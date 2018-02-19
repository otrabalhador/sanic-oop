from sanic.handlers import ErrorHandler

from error_handler.not_found_handler import Error404Handler
from error_handler.server_error_handler import ServerErrorHander


class ErrorHandlerCollection(ErrorHandler):
    def __init__(self):
        super().__init__()
        self.handlers_obj = [Error404Handler, ServerErrorHander]
        self.handlers = self._get_handlers()

    def _get_handlers(self):
        handlers = []
        for handler_obj in self.handlers_obj:
            handlers.append(
                handler_obj().get_error_handler()
            )
        return handlers
