#elements carrying attributes as a dict
from lxml import etree

#setting an attribute for the root element
root = etree.Element("root", interesting = "totally")
print etree.tostring(root)

print root.get("interesting")

print root.get("hello")

root.set("hello", "Huhu")
print root.get("hello")

print etree.tostring(root)

print  sorted(root.keys())

