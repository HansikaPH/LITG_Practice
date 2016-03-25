import re

p = re.compile('ab*')
print p

p = re.compile('ab*', re.IGNORECASE) #passing an optional flag argument
print p