'''
Created on Jun 14, 2012
	Generates cards and player hands
@author: sharvey3
'''
import random

class newcard():
	'''
	Randomly generate a card
	'''

	random.seed()

	def __init__(self):
		'''
		Constructor
		'''
		
		# All the "labels" possible - not their values
		labels = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
		
		# Suit doesn't matter as there are multiple cards in a shoe
		# Also pick a random label
		self.suit = random.choice('CHSD')
		self.label = random.choice(labels)
		
		# Convert 10, J, Q, K (strings in labels set) to numeric 10
		if self.label in ('10', 'J', 'Q', 'K'):
			self.value = 10
		else:
			self.value = self.label
			
		self.display = self.label + self.suit
		

# ----------------------------------
		
		
class playerhand():
	'''
	Generate a player's hand from 2 cards
	'''
		
	def __init__(self, handtype = "all"):

		c1 = newcard()
		c2 = newcard()
		
		tests = 0
		
		while validhand(c1, c2, handtype) == False:
			c1 = newcard()
			c2 = newcard()
			tests += 1
			
		print "Tests:", tests


		# If card two is an ace, swap it to card #1
		# (both for lookup purpose & to be easy on players)
		c2value = c2.value
		if c2value == "A":
			c3 = newcard()
			c3 = c1
			c1 = c2
			c2 = c3
			
		# Compile the hand's "lookup" value to match the keys found
		# in the YAML strategy table (15, A4, 77, etc.)
		if c1.value == c2.value:
			self.lookup = str(c1.value) + str(c2.value)
		elif c1.value == 'A':
			self.lookup = 'A' + str(c2.value)
		else:
			self.lookup = int(c1.value) + int(c2.value)
			
		self.lookup = str(self.lookup)
		# And, at long last, a nicely printable version of your hand
		self.display = c1.display + " " + c2.display
		
	
	
	
				
# ---------------------------
			
class dealercard(newcard):
	'''
	Simple: get a card for the dealer
	'''
	
	def __init__(self):
		dcard = newcard()
		self.value = str(dcard.value)
		self.display = dcard.display
	

# --------------------------

def validhand(c1, c2, handtype):

#		There has got to be a better way to handle this, probably by
#		changing the card values directly, instead of getting new hands.
		
		
		if handtype == "all":
			
			if c1.value == 10 and c2.value == 10:
				return False
			elif c1.value == 5 and c2.value == 5:
				return False
			elif c1.value == "A" and c2.value == 10:
				return False
			elif c1.value == 10 and c2.value == "A":
				return False
			else:
				return True	
			
			
		elif handtype == "hard":
			
			if c1.value == c2.value:
				return False
			elif c1.value == "A" or c2.value == "A":
				return False
			else:
				return True

			
		elif handtype == "soft":
			if (c1.value == "A" or c2.value == "A") and \
				(c1.value != 10 and c2.value != 10):
					return True
			else:
				return False

	
		elif handtype == "split":
			if c1.value != c2.value:
				return False
			elif c1.value == 10 or c1.value == "5":
				return False
			elif c1.value == "5" and c2.value == "5":
				return False
			else:
				return True
			
			

			