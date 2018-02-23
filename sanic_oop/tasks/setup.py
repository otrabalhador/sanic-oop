from sanic import Sanic


class SanicTaskSetup:
    def __init__(self, app: Sanic, tasks: list):
        self.__app = app
        self.__tasks = tasks

    def setup(self):
        for task in self.__tasks:
            self._add_task(task)

    def _add_task(self, task):
        self.__app.add_task(task)
