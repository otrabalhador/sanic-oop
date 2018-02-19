from middlewares.api_middleware import SanicMiddleware


class MiddlewareComposite:
    MIDDLEWARE = "middleware"
    ATTACH_TO = "attach_to"

    def __init__(self, middlewares: list):
        self.middlewares = middlewares

    def add(self, middleware: SanicMiddleware):
        self.middlewares.append(middleware)

    def get_registration_kwargs(self) -> dict():
        middlewares = []
        for middleware in self.middlewares:
            middlewares.append({
                self.MIDDLEWARE: middleware.middleware,
                self.ATTACH_TO: middleware.attach_to
            })
        return middlewares
