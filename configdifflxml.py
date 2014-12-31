#!/usr/bin/env python3

import collections
import re
import sys

from lxml import etree
from operator import itemgetter
from pprint import pprint as pp


## parse() returns an ElementTree object
parser = etree.XMLParser()

# ElementTree
#tree = etree.parse('b10f.xml')
tree = etree.parse('b11f.xml')

# Element
root = tree.getroot()

# 'export'
#print(root.tag)

# sort by element tag (what I think of as name) first
for parent in root.xpath('//*[./*]'):
    parent[:] = sorted(parent, key=lambda x: x.tag)

# The child elements of the root are already ordered by tag. We can also get
# the id of each child element. Combined, they make a unique identifier we can
# use for sorting. But how to do a two-level sort, first by element name, and
# then by id?

# The child elements of the root are already ordered by tag. Now order each
# element with the same tag (e.g., script-group, job-config, etc) by ID.
element_list = []
odict = collections.OrderedDict()

for elem in root.iterchildren():
    tmp_tag = elem.tag
    tmp_attr = int(elem.attrib.get('id'))
    element_list.append((tmp_tag, tmp_attr, etree.tostring(elem)))
    odict[tmp_tag] = elem.attrib

# this is really ugly, but it may be progress
for elem in sorted(element_list, key=itemgetter(0, 1)):
    print(elem)

