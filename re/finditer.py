#finditer method of re module
import re

p = re.compile('\d+')
iterator = p.finditer('12 drummers drumming, 11 ... 10 ...') #returns the matched strings in an iterator as a sequence of match objects
print iterator

for match in iterator:
    print match.span() #calling methods on each and every match object