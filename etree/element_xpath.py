#using xpath to read the text of elements
from lxml import etree

html = etree.Element("html")
body = etree.SubElement(html, "body")
body.text = "TEXT"

print etree.tostring(html)

br = etree.SubElement(body, "br")
print etree.tostring(html)

br.tail = "TAIL"
print etree.tostring(html,  pretty_print=True)

#extracting the text content of a tree as one whole concatenated string
print html.xpath("string()")

#extracting the text content as a list
print html.xpath("//text()")

#wrapping it in a function
build_text_list = etree.XPath("//text()")
print build_text_list(html)