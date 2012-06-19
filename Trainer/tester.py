'''
Created on Jun 19, 2012

@author: sharvey3
'''
import cards
import strategy

chart = strategy.table()

for i in range(1,50):
	
	h = cards.playerhand("split")
	d = cards.dealercard()
	correct = chart.get_correct(h.lookup, d.value)
		
	print "XX", d.display
	print h.display
	print correct
	print "---"
	print
	
	
	i += 1