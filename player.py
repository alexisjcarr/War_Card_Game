class Player:
    def __init__(self, id) -> None:
        self.id = id
        self.cards = []


    def play_card(self):
        return self.cards.pop(0)
