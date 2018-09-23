###Exrea Credit 1 Writing your own class/tests
import random


class Card(object):
    suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
    rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    def __init__(self, suit=0, rank=2):
        self.suit = self.suit_names[suit]
        self.rank = rank
        self.rank_num = rank # To handle winning comparison

    def __str__(self):
        return "{} of {}".format(self.rank_num,self.suit)


class Deck(object):
    def __init__(self): # Don't need any input to create a deck of cards
        # This working depends on Card class existing above
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card) # appends in a sorted order

    def __str__(self):
        total = []
        for card in self.cards:
            total.append(card.__str__())
        # shows up in whatever order the cards are in
        return "\n".join(total) # returns a multi-line string listing each card

    def pop_card(self, i=-1):
        return self.cards.pop(i) # this card is no longer in the deck -- taken off

    def shuffle(self):
        random.shuffle(self.cards)

    def replace_card(self, card):
        card_strs = [] # forming an empty list
        for c in self.cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.cards.append(card) # append it to the list

    def sort_cards(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

    def deal_hand(self, hand_size):
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.pop_card(i))
        return hand_cards

    def is_empty(self):
        if len(self.cards) == 0:
            return True
        else:
            return False
###################################################################
######################            Hand           #################
###################################################################
class Hand(object):
    def __init__(self, init_cards):
        self.cards = init_cards
        self.books = {}
        self.books_num = 0
    def add_card(self, card):
        add = -1
        for i in range(len(self.cards)):
            if self.cards[i].suit == card.suit and  self.cards[i].rank == card.rank:
                add = 1
        if add == -1:
            self.cards.append(card)
            if not self.books.__contains__(card.rank):
                self.books[card.rank] = 1
            else:
                self.books[card.rank] += 1
                if self.books[card.rank]== 4:
                    self.book_num += 1

    def remove_card(self, card):
        delete = -1
        for i in range(len(self.cards)):
            if self.cards[i].suit == card.suit and  self.cards[i].rank == card.rank:
                delete = i
        if delete != -1:
            del self.cards[delete]

    def draw(self, deck):
        drawCard = deck.pop_card()
        self.cards.append(drawCard)

    def take_away(self, card_number):
        res = []
        i = 0
        while i < len(self.cards):
            if card_number == self.cards[i].rank:
                res.append(self.cards.pop(i))
            i += 1
        return res

    def contain(self, card_number):
        for i in range(len(self.cards)):
            if card_number == self.cards[i].rank:
                return True
        return False

def game():
    deck = Deck()
    deck.shuffle()
    hand_1 = Hand(deck.deal_hand(7))
    hand_2 = Hand(deck.deal_hand(7))
    print_all_hands(hand_1, hand_2)
    ask_for_cards(deck, hand_1, hand_2)
    score_1 = hand_1.book_num
    score_2 = hand_2.book_num
    print (score_1)
    print (score_2)


def print_all_hands(hand_1, hand_2):
    print("++++++++++++++++++")
    print("Player 1")
    for card in hand_1.cards:
        print (card)
    print("=====================")
    print("Player 2")
    for card in hand_2.cards:
        print (card)
    print("++++++++++++++++++")

def ask_for_cards(deck, hand_1, hand_2):
    while not deck.is_empty():
        # player 1
        answer = int(input("Hello, Player 1! Please choose a card rank you would like to ask the other player if they have (between 1-13):"))
        while not hand_1.contain(answer):
            answer = int(input("You don't have any card with this rank! Please choose a card rank you would like to ask the other player if they have (between 1-13):"))
        all_matches = hand_2.take_away(answer)
        while len(all_matches) != 0:
            for card in all_matches:
                hand_1.add_card(card)
            print_all_hands(hand_1, hand_2)
            answer = int(input("Lucky! Once Again! Please choose a card rank you would like to ask the other player if they have (between 1-13):"))
            all_matches = hand_2.take_away(answer)
        if len(all_matches) == 0:
            print("draw a card from the deck")
            hand_1.draw(deck)
            print_all_hands(hand_1, hand_2)
            if deck.is_empty():
                break
        # player 2
        answer = int(input("Hello, Player 2! Please choose a card rank you would like to ask the other player if they have (between 1-13):"))
        while not hand_2.contain(answer):
            answer = int(input("You don't have any card with this rank! Please choose a card rank you would like to ask the other player if they have (between 1-13):"))
        all_matches = hand_1.take_away(answer)
        while len(all_matches) != 0:
            for card in all_matches:
                hand_2.add_card(card)
            print_all_hands(hand_1, hand_2)
            answer = int(input("Lucky! Once Again! Please choose a card rank you would like to ask the other player if they have (between 1-13):"))
            all_matches = hand_1.take_away(answer)
        if len(all_matches) == 0:
            print("draw a card from the deck")
            hand_2.draw(deck)
            print_all_hands(hand_1, hand_2)
            if deck.is_empty():
                break

game()

