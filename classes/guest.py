class Guest:
    def __init__(self, name, age, fave_song, wallet):
        self.name = name
        self.age = age
        self.fave_song = fave_song
        self.wallet = wallet
    
    def guest_name(self):
        return "Patrick Mahomes"

    def customer_has_money(self):
        return 50