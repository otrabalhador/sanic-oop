from sanic.handlers import ErrorHandler


class ErrorHandlerCollection(ErrorHandler):
    def __init__(self, error_handlers):
        super().__init__()
        self.handlers_obj = error_handlers
        self.handlers = self._get_handlers()

    def _get_handlers(self):
        handlers = []
        for handler_obj in self.handlers_obj:
            error_handlers = handler_obj().get_error_handlers()
            self._add_error_handlers(handlers, error_handlers)
        return handlers

    @staticmethod
    def _add_error_handlers(handlers, error_handlers):
        if isinstance(error_handlers, list):
            handlers.extend(error_handlers)
        else:
            handlers.append(error_handlers)
