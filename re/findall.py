#findall method of re module
import re

p = re.compile('\d+')
match = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping') #returns the matched strings as a list
print match

