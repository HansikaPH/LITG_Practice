#elements carrying text
from lxml import etree

root = etree.Element("root")
root.text = "TEXT"

print etree.tostring(root)