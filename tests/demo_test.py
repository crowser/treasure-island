# coding: utf-8
from unittest import TestCase


class DemoTestCase(TestCase):
    def test_demo(self):
        self.assertEqual("a", "a")
