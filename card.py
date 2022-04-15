from enum import Enum


class Suite(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

JOKER = 'JOKER'


class Card:
    def __init__(self, suite, value, special_name=None) -> None:
        self.suite = suite
        self.special_name = special_name
        self.value = value


    def __repr__(self) -> str:
        if self.suite == JOKER:
            return f'{self.suite}'
        elif self.special_name:
            return f'{self.special_name} of {self.suite}'
        return f'{self.value} of {self.suite}'
