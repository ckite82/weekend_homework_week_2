class Room:
    
    def __init__(self, guest, song, room_theme, guest_total, song_playlist):
        self.guest = guest
        self.song = song
        self.room_theme = room_theme
        self.room_guest_total = []
        self.song_playlist = []

    def room_has_theme(self):
        return "Classic Rock"

    def guests_in_room_total(self):
        return len(self.room_guest_total)

    def add_guest(self, guest_to_add):
        self.room_guest_total.append(guest_to_add)

    def remove_guest(self, guest_to_remove):
        self.room_guest_total.remove(guest_to_remove)

    def songs_in_playlist(self):
        return len(self.song_playlist)

    def add_song(self, song_to_add):
        self.song_playlist.append(song_to_add)