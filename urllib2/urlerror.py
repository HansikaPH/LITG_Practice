#handling urlerror
import urllib2

req = urllib2.Request('http://www.pretend_hansika.org')

try: urllib2.urlopen(req)
except URLError as e:
    print e.reason

