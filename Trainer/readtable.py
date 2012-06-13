'''
Created on Jun 13, 2012

@author: sharvey3
'''


import re
import yaml

stream = file('table.yml', 'r')
table = yaml.load(stream)

print table