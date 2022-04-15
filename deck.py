import random
from typing import *

from card import Card, JOKER, Suite


class Deck:
    def __init__(self) -> None:
        self.cards = self._generate_deck()


    def shuffle_deck(self) -> None:
        random.shuffle(self.cards)


    def _generate_deck(self) -> List[Card]:
        value_to_special_name_map: Dict[int, str] = {
            11: 'JACK',
            12: 'QUEEN',
            13: 'KING',
            14: 'ACE'
        }

        deck: List[Card] = [Card(JOKER, 15) for _ in range(2)]

        for suite in Suite:
            for value in range(2, 15):
                if value <= 10:
                    deck.append(Card(suite.name, value)) 
                else:
                    deck.append(Card(suite.name, value, value_to_special_name_map[value]))

        return deck
