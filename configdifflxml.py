#!/usr/bin/env python3

try:
  from lxml import etree
#  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")

from pprint import pprint as pp
import sys


# ----------------------------------------------------------------------------
#
## parse() returns an ElementTree object
parser = etree.XMLParser()

# ElementTree
#tree = etree.parse('b10f.xml')
tree = etree.parse('b11f.xml')
# Element
root = tree.getroot()
# 'export'
#print(root.tag)

#print(type(tree))
#print(type(root))
#sys.exit(0)

#print('root.tag:{}'.format(root.tag))
#print('root.attrib:{}'.format(root.attrib))
#
# ----------------------------------------------------------------------------

#print(etree.tostring(root))
#
#f = open('tree.xml', 'w')
#f.write(etree.tostring(root))

# ----------------------------------------------------------------------------
#
#parser2 = etree.XMLParser(ns_clean=True)
#tree2 = etree.parse('builder10.xml')
#
#root2 = tree2.getroot()
#
#f2 = open('tree_nsclean.xml', 'w')
#f2.write(etree.tostring(root))
#
# ----------------------------------------------------------------------------

# tree.iter() returns a ...
#for elem in tree.iter():
#  print('element:{}'.format(elem.tag))
#  print('  attrib:{}'.format(elem.attrib))
#  print('  text:{}'.format(elem.text))

#for elem in root.iterancestors():
#for elem in root.itersiblings():
#for elem in root.iterdescendants():

#for elem in root.iterchildren():
#    print('element:{}'.format(elem.tag))
#    print('  attrib:{}'.format(elem.attrib))
#    print('  text:{}'.format(elem.text))

#print(type(root.getchildren()))
#
#children = root.getchildren()
#children.sort(key='tag')
#
#for child in children:
#    print(child.tag)

#  item = {}
#  for elem in ia:
#    item[elem.tag] = elem.text.strip()
#  pp(item)

#doc = etree.XML(data, etree.XMLParser(remove_blank_text=True))
#for parent in doc.xpath('//*[./*]'):	# search for parent elements
#    parent[:] = sorted(parent, key=lambda x: x.tag)
for parent in root.xpath('//*[./*]'):	# search for parent elements
    parent[:] = sorted(parent, key=lambda x: x.tag)

#print(etree.tostring(root, method='xml', pretty_print=True))
#print(etree.tostring(root))
#print(etree.tostring(doc, method='xml', pretty_print=True))
#print(etree.tostring(doc))

#for parent in root.xpath('//*[./*]'):	# search for parent elements
#    parent[:] = sorted(parent, key=lambda x: x.attrib)


# The child elements of the root are already ordered by tag. Now order each
# element with the same tag (e.g., script-group, job-config, etc) by ID.
children_dict = {}
for elem in root.iterchildren():
    tmp_tag = elem.tag + "_" + elem.attrib.get('id')
    children_dict[tmp_tag] = elem
    #children_dict[tmp_tag] = [elem.tag, elem.attrib, elem.attrib.get('id')]
#    print('tmp_tag:{}'.format(tmp_tag))
#    print('  element:{}'.format(elem.tag))
#    print('    attrib:{}'.format(elem.attrib))
#    print('    attrib.id:{}'.format(elem.attrib.get('id')))
#    print('    text:{}'.format(elem.text))

print(sorted(children_dict.items()))
#print(sorted(children_dict.items(), key=lambda x: (x[1], x[0])))

