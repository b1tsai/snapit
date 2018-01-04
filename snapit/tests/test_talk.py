from unittest import TestCase

import snapit

class TestTalk(TestCase):
    def test_is_string(self):
        s = snapit.talk()
        self.assertTrue(isinstance(s, str))