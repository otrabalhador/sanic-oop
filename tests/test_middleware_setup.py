import unittest
from collections import deque

from sanic_oop import SanicOOP, OnRequestMiddleware, OnResponseMiddleware
from sanic_oop.middlewares.setup import MiddlewareSetup


class FakeMiddleware1(OnRequestMiddleware):
    def __init__(self):
        super().__init__(self.middleware)

    @staticmethod
    def middleware(request):
        pass


class FakeMiddleware2(OnResponseMiddleware):
    def __init__(self):
        super().__init__(self.middleware)

    @staticmethod
    def middleware(request):
        pass


class TestMiddlewareSetup(unittest.TestCase):
    def test_setup_middlewares(self):
        """
            Asserts that MiddlewareSetup correctly assigns
            middlewares to instance of Sanic app.
            It should assign request and response middleware
            accordingly to Sanic app instance variables:
                - request_middleware
                - response_middleware
        """
        # Input
        app = SanicOOP()
        middleware_objects = [FakeMiddleware1, FakeMiddleware2]

        # Expected
        expected_request_middleware = deque([FakeMiddleware1.middleware])
        expected_response_middleware = deque([FakeMiddleware2.middleware])

        # Call
        MiddlewareSetup(app, middleware_objects).setup_middlewares()

        # Assertion
        self.assertEqual(app.request_middleware, expected_request_middleware)
        self.assertEqual(app.response_middleware, expected_response_middleware)
