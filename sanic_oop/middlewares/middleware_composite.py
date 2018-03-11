from sanic_oop.middlewares.api_middleware import SanicOOPMiddleware


class MiddlewareComposite:
    MIDDLEWARE = "middleware"
    ATTACH_TO = "attach_to"

    def __init__(self, middlewares: list):
        self.middlewares = middlewares

    def add(self, middleware: SanicOOPMiddleware):
        self.middlewares.append(middleware)

    def get_registration_kwargs(self) -> dict():
        middlewares = []
        for middleware_object in self.middlewares:
            middleware_instance = middleware_object()
            middlewares.append({
                self.MIDDLEWARE: middleware_instance.middleware,
                self.ATTACH_TO: middleware_instance.attach_to
            })
        return middlewares
