from api import app_routes, blueprints
from api.common.error_handler import error_handlers
from api.common.listeners import ListenerCollection
from api.common.middlewares import middleware_objects
from sanic_oop import SanicAppSetup
from tasks import SanicTaskCollection


class AppSetup(SanicAppSetup):
    def __init__(self, app):
        super().__init__(app)
        self.app_middlewares = middleware_objects
        self.app_listeners = ListenerCollection
        self.app_routes = app_routes
        self.app_tasks = SanicTaskCollection
        self.blueprints = blueprints
        self.error_handlers = error_handlers
