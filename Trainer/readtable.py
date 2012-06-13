'''
Created on Jun 13, 2012

@author: sharvey3
'''


import re
import yaml
import random

stream = file('table.yml', 'r')
table = yaml.load(stream)
stream.close()

plays = ({})

d_cards = re.split(' ', "2 3 4 5 6 7 8 9 10 A")

for p_hand in table.keys():
		
	p_plays = re.split(' *', table[p_hand])

	i = 0

	for d_has in d_cards:
	
		p_play = p_plays[i]
		
		plays[p_hand, d_has] = p_play

		i += 1


random.seed()

for tests in range(1,20):
	
	p_hand = random.choice(table.keys())
	d_has = random.choice(d_cards)
	correct = plays[p_hand, d_has]
	
	print "P: %s	D: %s	Do: %s" % (p_hand, d_has, correct)
	
	
	

