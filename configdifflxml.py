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

from operator import itemgetter
from pprint import pprint as pp
import collections
import re
import sys


# http://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside
#def atoi(text):
#    return int(text) if text.isdigit() else text
#
#def natural_keys(text):
#    '''
#    alist.sort(key=natural_keys) sorts in human order
#    http://nedbatchelder.com/blog/200712/human_sorting.html
#    (See Toothy's implementation in the comments)
#    '''
#    return [ atoi(c) for c in re.split('(\d+)', text) ]
#
# Works okay for non-negative integers, but not negative ones like -2.
#
#alist=[
#    "something1",
#    "something12",
#    "something17",
#    "something2",
#    "something-2",
#    "something25",
#    "something29"]
#
#alist.sort(key=natural_keys)
#print(alist)
#sys.exit(0)


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

#  item = {}
#  for elem in ia:
#    item[elem.tag] = elem.text.strip()
#  pp(item)

#doc = etree.XML(data, etree.XMLParser(remove_blank_text=True))
for parent in root.xpath('//*[./*]'):	# search for parent elements
    parent[:] = sorted(parent, key=lambda x: x.tag)

# The child elements of the root are already ordered by tag. We can also get
# the id of each child element. Combined, they make a unique identifier we can
# use for sorting. But how to do a two-level sort, first by element name, and
# then by id?

# The child elements of the root are already ordered by tag. Now order each
# element with the same tag (e.g., script-group, job-config, etc) by ID.
#children_dict = {}
element_list = []
odict = collections.OrderedDict()

for elem in root.iterchildren():
    #tmp_tag = elem.tag + "_" + elem.attrib.get('id')
    tmp_tag = elem.tag
    tmp_attr = int(elem.attrib.get('id'))
    element_list.append((tmp_tag, tmp_attr))
#    children_dict[tmp_tag] = elem
    odict[tmp_tag] = elem.attrib
    #children_dict[tmp_tag] = [elem.tag, elem.attrib, elem.attrib.get('id')]
#    print('tmp_tag:{}'.format(tmp_tag))
#    print('  element:{}'.format(elem.tag))
#    print('    attrib:{}'.format(elem.attrib))
#    print('    attrib.id:{}'.format(elem.attrib.get('id')))
#    print('    text:{}'.format(elem.text))

#print(type(children_dict))
#for k, v in children_dict.items():
#    print(k, v)
#print('#----------------------------------------------\n\n')
#for k, v in odict.items():
#    print(k, v)

# inspect the list
#print(element_list)

# Doesn't sort numbers correctly (wah wah) but at least it's consistent. May
# want to use the natural_keys sort above.
for elem in sorted(element_list, key=itemgetter(0, 1)):
    print(elem)

#print(sorted(element_list))
#alist.sort(key=natural_keys)

#print(sorted(children_dict.items()))
#print(sorted(children_dict.items(), key=lambda x: (x[1], x[0])))

