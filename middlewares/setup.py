from middlewares.middleware_composite import MiddlewareComposite
from middlewares.print_on_request import PrintOnRequestMiddleware
from middlewares.print_on_response import PrintOnResponseMiddleware


class SetupMiddlewares:
    def __init__(self, app):
        self.app = app
        middleware_instances = [PrintOnResponseMiddleware(), PrintOnRequestMiddleware()]
        self.middleware_composite = MiddlewareComposite(middleware_instances)

    def setup_middlewares(self):
        for middleware_kwargs in self.middleware_composite.get_registration_kwargs():
            self._register_middlewares(middleware_kwargs)

    def _register_middlewares(self, middleware_kwargs):
        self.app.register_middleware(**middleware_kwargs)
