from sanic import Sanic
from sanic_cors import CORS
from sanic_openapi import swagger_blueprint, openapi_blueprint

from sanic_oop.error_handler.error_handler import ErrorHandlerCollection
from sanic_oop.listeners.setup import ListenerSetup
from sanic_oop.middlewares.setup import MiddlewareSetup
from sanic_oop.tasks.setup import SanicTaskSetup


class SanicAppSetup:

    def __init__(self, app: Sanic):
        self.__app = app
        self.app_middlewares = None
        self.app_listeners = None
        self.app_routes = None
        self.app_tasks = None
        self.blueprints = None
        self.error_handlers = None

    def setup(self):
        self._setup_blueprints()
        self._setup_cors()
        self._setup_routes()
        self._setup_exceptions()
        self._setup_middlewares()
        self._setup_listeners()
        self._setup_tasks()
        self._setup_openapi_swagger()

    def _setup_blueprints(self):
        for blueprint in self.blueprints:
            blueprint().setup(self.__app)

    def _setup_cors(self):
        CORS(self.__app)

    def _setup_routes(self):
        if self.app_routes:
            self.app_routes.start_routes(self.__app)

    def _setup_exceptions(self):
        self.__app.error_handler = ErrorHandlerCollection(self.error_handlers)

    def _setup_middlewares(self):
        if self.app_middlewares:
            MiddlewareSetup(self.__app, self.app_middlewares).setup_middlewares()

    def _setup_listeners(self):
        if self.app_listeners:
            listeners = self.app_listeners().listeners
            ListenerSetup(self.__app, listeners).setup_listeners()

    def _setup_tasks(self):
        if self.app_tasks:
            tasks = self.app_tasks().tasks
            SanicTaskSetup(self.__app, tasks).setup()

    def _setup_openapi_swagger(self):
        self.__app.blueprint(openapi_blueprint)
        self.__app.blueprint(swagger_blueprint)
