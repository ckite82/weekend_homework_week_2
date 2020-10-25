import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Patrick Mahomes", 25, "Hotel California")

    def test_guest_has_name(self):
        self.assertEqual("Patrick Mahomes", self.guest_1.guest_name())