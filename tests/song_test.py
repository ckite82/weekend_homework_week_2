import unittest
from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Hotel California", "Classic Rock")

    def test_song_has_name(self):
        self.assertEqual("Hotel California", self.song.display_name())