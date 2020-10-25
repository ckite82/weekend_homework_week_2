import unittest
from classes.guest import *
from classes.song import *
from classes.room import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Patrick Mahomes", 25, "Hotel California", 50)
        self.guest_2 = Guest("Barry Sanders", 52, "Highway to Hell", 30)
        self.guest_3 = Guest("Drew Brees", 41, "Born in the USA", 100)
        self.guest_4 = Guest("Matt Ryan", 35, "Black Betty", 60)
        self.guest_5 = Guest("Aaron Rodgers", 36, "Born to be Wild", 20)
        self.guest_6 = Guest("Tom Brady", 43, "Ace of Spades", 35)
        self.song_1 = Song("Hotel California", "Classic Rock")
        self.song_2 = Song("Highway to Hell", "Classic Rock")
        self.song_3 = Song("Born in the USA", "Classic Rock")
        self.song_4 = Song("Black Betty", "Classic Rock")
        self.song_5 = Song("Born to be Wild", "Classic Rock")
        self.song_6 = Song("Ace of Spades", "Classic Rock")
        self.room = Room(self.guest_1, self.song_1, "Classic Rock", 0, 0)
# I thought that after I added the extra guests and songs in, 
# that in the self.room() parameter I would need to add them all in there as well, 
# e.g self.guest_2, self.song_4, etc...but the tests seemed to pass with just
# entering self.guest_1, and self.song_1, although keeping it as self.guest and self.song
# would fail the tests. Played around with tests and all OK

    def test_room_has_theme(self):
        self.assertEqual("Classic Rock", self.room.room_has_theme())

    def test_room_starts_empty(self):
        self.assertEqual(0, self.room.guests_in_room_total())

    def test_add_guest_to_room(self):
        # guest = Guest("Patrick Mahomes", 25, "Hotel California") this line not needed, call on self.guest instead of guest.
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_2)
        self.assertEqual(2, self.room.guests_in_room_total())

    def test_remove_guest_from_room(self):
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_2)
        self.room.add_guest(self.guest_3)
        self.room.remove_guest(self.guest_1)
        self.room.remove_guest(self.guest_2)
        self.room.remove_guest(self.guest_3)
        self.assertEqual(0, self.room.guests_in_room_total())

    def test_playlist_starts_empty(self):
        self.assertEqual(0, self.room.songs_in_playlist())

    def test_add_song_to_playlist(self):
        self.room.add_song(self.song_1)
        self.room.add_song(self.song_2)
        self.room.add_song(self.song_5)
        self.assertEqual(3, self.room.songs_in_playlist())

    # def test_room_occupancy_level(self):
    #     self.room.add_guest(self.guest_1)
    #     self.room.add_guest(self.guest_2)
    #     self.room.add_guest(self.guest_3)
    #     self.room.add_guest(self.guest_4)
    #     self.assertEqual(4, self.room.max_occupancy())