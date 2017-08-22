import random

SUITS = {'Spades', 'Clubs', 'Hearts', 'Diamonds'}
TYPE = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}

# Use a Python dictionary to store values specific to BlackJack
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

class Card:
	
	def __init__(self, suit, type):
		self.suit = suit
		self.type = type

	def get_suit(self):
		return self.suit

	def get_type(self):
		return self.type

	def get_value(self):
		return VALUES[self.type]

class Deck:
	
	def __init__(self):
		for suit in SUITS:
			for type in TYPE:
				self.deck.append(Card(suit, type)

	def shuffle(self):
		random.shuffle(self.deck)

	def take_card(self):
		self.deck.pop(0)

class Game:

	def __init__(self):
		self.player_hand = []
		self.dealer_hand = []
		self.hold = False

	def start_game(self):
		self.deck = Deck()
		self.deck = self.deck.shuffle()
		
		self.player_hand.append(self.deck.pop(0))
		self.player_hand.append(self.deck.pop(0))
		self.dealer_hand.append(self.deck.pop(0))
		self.dealer_hand.append(self.deck.pop(0))

	
	def play_game(self):
		self.start_game()

		while self.hold is False:
			if(np.sum(self.player_hand) > 21):
				println("LOSER; over 21")
				return
			elif(np.sum(self.player_hand) == 21 and np.sum(self.dealer_hand) != 21):
				println("21! YOU WIN")
				return
			elif(np.sum(dealer_hand) == 21):
				println("DEALER HAS 21; YOU LOSE")
				return
			else:
				println("Score is: " + np.sum(self.player_hand))
				x = raw_input("Hold? (type y or n)")
				if x is 'n':
					self.hold = True
				else:
					self.player_hand.append(self.deck.pop(0))

		if(np.sum(self.player_hand) > np.sum(self.dealer_hand)):
			println("WINNER")
			return
		else:
			println("LOSER")
			return
