#creating custom parsers
from io import BytesIO
from lxml import etree

#creating a custom XMLParser
parser = etree.XMLParser(remove_blank_text=True) #parser that removes empty text between tags while parsing
root = etree.XML("<root>  <a/>   <b>  </b>     </root>", parser)
print etree.tostring(root)

#creating an HTMLParser
parser = etree.HTMLParser();
tree = etree.parse(BytesIO("<html><head></head><body><p>Hello<br>World</p></body></html>"), parser)
print etree.tostring(tree)