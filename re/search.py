#search method of re module
import re

p = re.compile('[a-z]+')

match1 = p.match('::: message')
print match1

match2 = p.search('::: message')
print match2

print match2.group()
print match2.span()