from sanic import Sanic
from sanic_cors import CORS
from sanic_openapi import swagger_blueprint, openapi_blueprint

import middlewares
import routes
from listeners import ListenerSetup, ListenerCollection
from tasks import SanicTaskCollection, SanicTaskSetup


class SanicAppSetup:
    def __init__(self, app: Sanic):
        self.__app = app

    def setup(self):
        self._setup_cors()
        self._setup_routes()
        self._setup_middlewares()
        self._setup_listeners()
        self._setup_tasks()
        self._setup_openapi_swagger()

    def _setup_cors(self):
        CORS(self.__app)

    def _setup_routes(self):
        routes.start_routes(self.__app)

    def _setup_middlewares(self):
        middlewares.MiddlewareSetup(self.__app, middlewares.middleware_objects).setup_middlewares()

    def _setup_listeners(self):
        listeners = ListenerCollection().listeners
        ListenerSetup(self.__app, listeners).setup_listeners()

    def _setup_tasks(self):
        tasks = SanicTaskCollection().tasks
        SanicTaskSetup(self.__app, tasks).setup()

    def _setup_openapi_swagger(self):
        self.__app.blueprint(openapi_blueprint)
        self.__app.blueprint(swagger_blueprint)
