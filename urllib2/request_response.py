#show the request-response behaviour of http
import urllib2
import urllib


#simple http request
req = urllib2.Request('https://docs.python.org/2/howto/urllib2.html') #creating a request object
response = urllib2.urlopen(req) #calling urlopen on the created request object
the_page = response.read()
print the_page

#http request with data as an argument
url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Hansika Hewamalage',
          'location' : 'Piliyandala',
          'language' : 'Python' }

data = urllib.urlencode(values) #data needs to be encoded in a standard way
req = urllib2.Request(url, data) #pass data to the request object as an argument
response = urllib2.urlopen(req)
the_page = response.read()
print the_page