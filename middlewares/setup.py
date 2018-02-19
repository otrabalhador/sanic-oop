from middlewares.lib_abstraction.middleware_composite import MiddlewareComposite


class SetupMiddlewares:
    def __init__(self, app, middleware_objects):
        self.app = app
        self.middleware_composite = MiddlewareComposite(middleware_objects)

    def setup_middlewares(self):
        for middleware_kwargs in self.middleware_composite.get_registration_kwargs():
            self._register_middlewares(middleware_kwargs)

    def _register_middlewares(self, middleware_kwargs):
        self.app.register_middleware(**middleware_kwargs)
