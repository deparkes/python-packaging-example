import unittest
from my_package import main

class TestMain(unittest.TestCase):
    def test_main(self):
        assert main.main() == "Hello, World"