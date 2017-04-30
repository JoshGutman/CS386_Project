from datetime import datetime

from game import Game
from card import Card

class Collection:

    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.cards = []
        self.creation_time = datetime.now()

    def add_card(card):
        self.cards.append(card)

    def __eq__(self, x):
        assert type(x) == Collection
        if self.name == x.name:
            return True
        else:
            return False
