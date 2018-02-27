import asyncio


class SanicTaskCollection:
    """
        This class contains tasks to be run in the background
        after loop has started.
        These will be scheduled right before the server start
    """

    def __init__(self):
        self.tasks = [self._notify_server_started_after_five_seconds]

    @staticmethod
    async def _notify_server_started_after_five_seconds():
        await asyncio.sleep(10)
        print('Rubinho Barrichello says: Server successfully started')
