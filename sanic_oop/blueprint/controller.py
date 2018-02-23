from sanic import Blueprint


class BlueprintController(Blueprint):
    def __init__(self, name, routes, exceptions=None, middlewares=None, listeners=None):
        self.__routes = routes
        self.__exceptions = exceptions
        self.__middlewares = middlewares
        self.__listeners = listeners
        super().__init__(name)

    def setup(self, app):
        self._setup_routes()
        self._setup_exceptions()
        self._setup_middlewares()
        self._setup_listeners()
        app.blueprint(self)

    def _setup_routes(self):
        route_object = self.__routes
        route_instance = route_object(self)
        route_instance.add_routes()

    def _setup_exceptions(self):
        pass

    def _setup_middlewares(self):
        pass

    def _setup_listeners(self):
        pass
