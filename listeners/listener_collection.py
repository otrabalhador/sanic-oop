class ListenerCollection(object):
    BEFORE_SERVER_START = 'before_server_start'
    AFTER_SERVER_START = 'after_server_start'
    BEFORE_SERVER_STOP = 'before_server_stop'
    AFTER_SERVER_STOP = 'after_server_stop'

    def __init__(self):
        self.listeners = {
            self.BEFORE_SERVER_START: self._before_server_start,
            self.AFTER_SERVER_START: self._after_server_start,
            self.BEFORE_SERVER_STOP: self._before_server_stop,
            self.AFTER_SERVER_STOP: self._after_server_stop,
        }

    @staticmethod
    def _before_server_start(app, loop):
        print("Heeeeey, look at mee!! I'm starting the server")

    @staticmethod
    async def _after_server_start(app, loop):
        print("Yupp!! Server has just been started")

    @staticmethod
    async def _before_server_stop(app, loop):
        print("It was nice, but everything has an end.")

    @staticmethod
    async def _after_server_stop(app, loop):
        print("xoxo")
