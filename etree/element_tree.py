#creating xml tree structure

from lxml import etree

root = etree.Element("root")
print root.tag #printing the xml tag name of the element

#creating a child element and adding it to the parent element.
root.append(etree.Element("child1"))

#alternative method to add child elements
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")

#printing the created xml tree
print etree.tostring(root, pretty_print=True)

#check whether a given item is an element
print etree.iselement(child2)