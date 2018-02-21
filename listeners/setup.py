from sanic import Sanic


class ListenerSetup:

    def __init__(self, app: Sanic, listeners: dict):
        self.__app = app
        self.__listeners = listeners

    def setup_listeners(self):
        for event, listener in self.__listeners.items():
            self._register_listener(listener, event)

    def _register_listener(self, listener, event):
        """
        --- Taken from sanic implementation that is not released yet

        Doc:
        Register the listener for a given event.

        Args:
            listener: callable i.e. setup_db(app, loop)
            event: when to register listener i.e. 'before_server_start'

        Returns: listener
        """

        self.__app.listener(event)(listener)
