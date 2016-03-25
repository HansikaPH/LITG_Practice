#match method of re module
import re

p = re.compile('[a-z]+')

match1 = p.match("")
print match1

match2 = p.match("tempo")
print match2

#trying out functions on the match object
print match2.group() #return the string matched by the RE
print match2.start() #return the starting position of the match
print match2.end() #return the ending position of the match. 1 + the actual last index
print match2.span() #Return a tuple containing the (start, end) positions of the match

