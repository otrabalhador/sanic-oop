import unittest
from sanic import Sanic
from sanic_oop import SanicOOP


class TestSanicOOP(unittest.TestCase):
    def test_is_instance_of_sanic(self):
        sanic_oop = SanicOOP()
        self.assertIsInstance(sanic_oop, Sanic)
