#GET request
import urllib2

#response is a file like object
response = urllib2.urlopen('https://docs.python.org/2/howto/urllib2.html')
print "Response", response

#get the url
print "The URL is: ", response.geturl()

# Getting the status code
print "This gets the code: ", response.code

# Get the Headers.
# This returns a dictionary-like object
print "The Headers are: ", response.info()

# Get the date of the header
print "The Date is: ", response.info()['date']

# Get the server of the header
print "The Server is: ", response.info()['server']

# Get all data
html = response.read()
print "Get all data: ", html

# Get the length of the data
print "Get the length :", len(html)

response.close()
