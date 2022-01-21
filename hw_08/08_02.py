"""
The game "Blackjack"
Conditions:
    2 types of decks: Large (56) and small (36 cards)
    2 modes: Single player, Single vs. Computer
    Players start with 2 random cards.
    Players may: Draw a card; End the move; Stop and announce your
    result; LoЫse.

    The player wins if: He has the sum of the numbers of cards in his
    hands is 21. If he has the highest sum of card numbers among all players
    (except in Single player).
    When a card is taken from the deck until the next game, it disappears.
"""

import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "".join((self.value, self.suit))


class Deck():
    def __init__(self, small=None, large=None):
        self.small = small
        self.large = large

    def deck_create(self, small=None, large=None):
        s_list = [u"\u2665", u"\u2666", u"\u2663", u"\u2660"]
        if self.large:
            v_list = ["A", "2", "3", "4", "5", "6", "7",
                      "8", "9", "10", "J", "Q", "K"]
        else:
            v_list = ["A", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(s, v) for s in s_list for v in v_list]

    def shuffle(self, small=None, large=None):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)


class Hand:
    def __init__(self, dealer=False, friend=False, bot=False):
        self.dealer = dealer
        self.bot = bot
        self.friend = friend
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self, dealer=None, friend=None, bot=None):
        if self.dealer:
            print('┌───────┐')
            print('|░░░░░░░|')
            print('|░░░░░░░|')
            print('|░░░░░░░|')
            print('|░░░░░░░|')
            print('|░░░░░░░|')
            print('└───────┘')

            print('┌───────┐')
            print('|{:<7}|'.format('{}'.format(self.cards[0])))
            print('|       |')
            print('|{:^7}|'.format('{}'.format(self.cards[0].suit)))
            print('|       |')
            print('|{:>7}|'.format('{}'.format(self.cards[0])))
            print('└───────┘')
        elif self.bot or self.friend:
            for i in range(2):
                print('┌───────┐')
                print('|░░░░░░░|')
                print('|░░░░░░░|')
                print('|░░░░░░░|')
                print('|░░░░░░░|')
                print('|░░░░░░░|')
                print('└───────┘')
        else:
            for i in range(len(self.cards)):
                print('┌───────┐')
                print('|{:<7}|'.format('{}'.format(self.cards[i])))
                print('|       |')
                print('|{:^7}|'.format('{}'.format(self.cards[i].suit)))
                print('|       |')
                print('|{:>7}|'.format('{}'.format(self.cards[i])))
                print('└───────┘')
            print("Value:", self.get_value())


class Game:

    def play(self):
        playing = True

        while playing:
            choice_deck = input(
                "Enter '1' to play small deck, '2' to play large deck:\n")
            if choice_deck == '1':
                self.deck = Deck(small=True)
            elif choice_deck == '2':
                self.deck = Deck(large=True)
            else:
                print("Enter '1' or '2'")
            self.deck.deck_create()
            self.deck.shuffle()

            choice_game_type = input(
                "Enter '1' to play single player, '2' to play with bot:\n")
            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)
            if choice_game_type == '2':
                self.bot_hand = Hand(bot=True)
            else:
                print("Enter '1' or '2'")

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())
                if choice_game_type == '2':
                    self.bot_hand.add_card(self.deck.deal())

            print("Dealer's hand is:")
            self.dealer_hand.display()
            if choice_game_type == '2':
                print("Bot hand is:")
                self.bot_hand.display()
            print("Your hand is:")
            self.player_hand.display()

            game_over = False

            while not game_over:
                (player_has_blackjack, dealer_has_blackjack,
                 bot_has_blackjack) = self.check_for_blackjack()
                if (player_has_blackjack or dealer_has_blackjack
                        or bot_has_blackjack):
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack,
                                                dealer_has_blackjack,
                                                bot_has_blackjack)
                    continue

                choice = input("Please choose [hit / stay] ").lower()
                while choice not in ["h", "s", "hit", "stay"]:
                    choice = input(
                        "Please enter 'hit' or 'stay' (or h/s) ").lower()
                if choice in ['hit', 'h']:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.dealer_hand.get_value() < 17:
                        self.dealer_hand.add_card(self.deck.deal())
                    if choice_game_type == '2' and self.bot_hand.get_value() < 17:
                        self.bot_hand.add_card(self.deck.deal())
                    if self.player_is_over():
                        print("You lose!")
                        game_over = True


                else:
                    if self.dealer_hand.get_value() < 17:
                        self.dealer_hand.add_card(self.deck.deal())
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()
                    if choice_game_type == '2':
                        bot_hand_value = self.bot_hand.get_value()

                    print("Final Results")
                    print("Your hand:", player_hand_value)
                    print("Dealer's hand:", dealer_hand_value)
                    if choice_game_type == '2':
                        print("Bot hand:", bot_hand_value)

                    if player_hand_value < 21:
                        flag = 0
                        if dealer_hand_value > 21:
                            flag += 1
                        if dealer_hand_value < 21 and \
                                player_hand_value > dealer_hand_value:
                            flag += 1
                        if choice_game_type == '2':
                            if bot_hand_value > 21:
                                flag += 1
                            if bot_hand_value < 21 and \
                                    player_hand_value > bot_hand_value:
                                flag += 1
                        if choice_game_type == '1' and flag == '1':
                            print("You win!")
                        if choice_game_type == '2' and flag == '2':
                            print("You win!")
                    else:
                        print("You lose!")

                    game_over = True

            again = input("Play Again? [y/n] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter 'y' or 'n' ")
            if again.lower() == "n":
                print("Goodbye!")
                playing = False
            else:
                game_over = False

    def player_is_over(self):
        return self.player_hand.get_value() > 21

    def check_for_blackjack(self):
        player = False
        dealer = False
        bot = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True
        try:
            if self.bot_hand.get_value() == 21:
                bot = True
        except AttributeError:
            pass

        return player, dealer, bot

    def show_blackjack_results(self, player_has_blackjack,
                               dealer_has_blackjack, bot_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack and \
                bot_has_blackjack:
            print("All players have blackjack! Draw!")

        elif player_has_blackjack:

            if bot_has_blackjack:
                print("Players have blackjack! Draw!")
            elif dealer_has_blackjack:
                print("Players have blackjack! Draw!")
            else:
                print("You have blackjack! You win!")

        elif dealer_has_blackjack:

            if bot_has_blackjack:
                print("Players have blackjack! Draw!")
            else:
                print("Dealer have blackjack!")

        elif bot_has_blackjack:
            print("Bot has blackjack!")


if __name__ == "__main__":
    g = Game()
    g.play()
