from unittest import TestCase

from snapit.command_line import main


class TestCmd(TestCase):
    def test_basic(self):
        main()