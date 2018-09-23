###Exrea Credit 1 Writing your own class/tests
class Card(object):
    suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
    rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

    def __init__(self, suit=0, rank=2):
        self.suit = self.suit_names[suit]
        if rank in self.faces: # self.rank handles printed representation
            self.rank = self.faces[rank]
        else:
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
###################################################################
######################            Hand           #################
###################################################################
class Hand(object):
    def __init__(self, init_cards):
        self.cards = init_cards
    def add_card(self, card):
        add = -1
        for i in range(len(self.cards)):
            if self.cards[i].suit == card.suit and  self.cards[i].rank == card.rank:
                add = 1
        if add == -1:
            self.cards.append(card)

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

def game_():
    deck = Deck()
    deck.shuffle()
    hand_1 = Hand(deck.deal_hand(7))
    hand_2 = Hand(deck.deal_hand(7))
    ask_for_cards(deck, hand_1, hand_2)
    score_1 = hand_1.count_score()
    score_2 = hand_2.count_score()
    print (score_1)
    print (score_2)
    
def ask_for_cards(deck, hand_1, hand_2):
    while not deck.is_empty():
        # player 1
        answer = input("Hello, Player 1! Please choose a card rank you would like to ask the other player if they have (between 1-13):")
        all_matches = hand_2.take_away(answer)
        while len(all_matches) != 0:
            for card in all_matches:
                hand_1.add_card(card)
            answer = input("Hello, Player 1! Please choose a card rank you would like to ask the other player if they have (between 1-13):")
            all_matches = hand_2.take_away(answer)
        if len(all_matches) == 0:
            hand_1.draw()
            if deck.is_empty():
                break
        # player 2
        answer = input("Hello, Player 2! Please choose a card rank you would like to ask the other player if they have (between 1-13):")
        all_matches = hand_1.take_away(answer)
        while len(all_matches) != 0:
            for card in all_matches:
                hand_2.add_card(card)
            answer = input("Hello, Player 2! Please choose a card rank you would like to ask the other player if they have (between 1-13):")
            all_matches = hand_1.take_away(answer)
        if len(all_matches) == 0:
            hand_2.draw()
            if deck.is_empty():
                break

game()

