import os
import time
from typing import *

from card import Card
from deck import Deck
from player import Player


class Game:
    def __init__(self) -> None:
        self.player_one = Player(1)
        self.player_two = Player(2)
        self.deck = Deck()

        self._deal_cards_to_players()


    def _deal_cards_to_players(self):
        self.deck.shuffle_deck()
        
        self.player_one.cards.extend(self.deck.cards[:27])
        self.player_two.cards.extend(self.deck.cards[27:])


    def get_current_winner(self) -> None:
        score_diff = self.get_score_diff()

        if score_diff == 0:
            print("\nYou are tied!")

        elif score_diff > 0:
            print(f"\nYou are up by {score_diff}")

        else:
            print(f"\nComputer is up by {abs(score_diff)}")


    def get_score_diff(self) -> int:
        return len(self.player_one.cards) - len(self.player_two.cards)


    def get_final_winner(self) -> None:
        score_diff = self.get_score_diff()

        if score_diff == 0:
            print("\nYou are tied!")

        elif score_diff > 0:
            print(f"\nYOU WIN!")

        else:
            print(f"\nCOMPUTER WINS!")


    @staticmethod
    def _generate_player_played_str(player_one_card: Card, player_two_card: Card) -> str:
        player_one_play_str, player_two_play_str = f"\nYou play {player_one_card}!", f"Computer plays {player_two_card}!"

        return player_one_play_str, player_two_play_str

    
    def play_turn(self) -> None:
        player_one_card, player_two_card = self.player_one.play_card(), self.player_two.play_card()
        winnings: List[Card] = [player_one_card, player_two_card]

        player_one_play_str, player_two_play_str = self._generate_player_played_str(player_one_card, player_two_card)
        print(player_one_play_str)
        print(player_two_play_str)

        while player_one_card.value == player_two_card.value:

            # 3 face down cards per player
            player_one_face_down_cards: List[Card] = [self.player_one.play_card() for _ in range(3)]
            player_two_face_down_cards: List[Card] = [self.player_two.play_card() for _ in range(3)]

            # 1 fighting card
            player_one_card: Card = self.player_one.play_card()
            player_two_card: Card = self.player_two.play_card()

            # add to winnings
            winnings.extend([*player_one_face_down_cards, *player_two_face_down_cards, player_one_card, player_two_card])

            player_one_play_str, player_two_play_str = self._generate_player_played_str(player_one_card, player_two_card)
            print(player_one_play_str)
            print(player_two_play_str)

        if player_one_card.value > player_two_card.value:
            print("\nYou win this turn!")
            self.player_one.cards.extend(winnings)

        else:
            print("\nComputer wins this turn!")
            self.player_two.cards.extend(winnings)

        self.get_current_winner()


if __name__ == '__main__':
    play_game = True

    game = Game()

    print("Hi welcome to War! Would you like to play this game in interactive mode? Y or N:     ")
    im = input()

    interactive_mode = True if im.upper() == 'Y' else False

    while play_game:
        game.play_turn()

        # set play_game to False if one player had 0 cards
        if game.get_score_diff() == abs(52):
            play_game = False

        if interactive_mode:
            print('\nPlay another turn? Y or N:   ')
            play_again = input()
            play_game = True if play_again.upper() == 'Y' else False

        else:
            time.sleep(3.5)

        os.system('cls' if os.name == 'nt' else 'clear')

    game.get_final_winner()
