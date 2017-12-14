import os
import unittest

from tangled.web import Application

from webtest import TestApp

default_config_file = os.path.join(os.getcwd(), 'test.ini')


def configure(config_file):
    global default_config_file
    default_config_file = config_file


class BaseTestCase(unittest.TestCase):

    def setUp(self, config_file=None):
        self.wsgi_app = Application(default_config_file)
        self.app = TestApp(self.wsgi_app)