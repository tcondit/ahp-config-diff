#!/usr/bin/env python3

# TODO to be most useful, we'll need to format the XML before sorting and
# printing it

import collections
import re
import sys

from lxml import etree
from operator import itemgetter
from pprint import pprint as pp


parser = etree.XMLParser()
#tree = etree.parse('b10f.xml')
#tree = etree.parse('b11f.xml')
# pretty print the XML before sorting (truly a work in progress)
# http://stackoverflow.com/questions/749796/pretty-printing-xml-in-python
tree = etree.parse('msb.xml', parser)
tree.write('msb_pp.xml', pretty_print=True, encoding='utf-8')
tree = etree.parse('msb_pp.xml')
root = tree.getroot()

# Sort child elements by tag (what I think of as name) first
for parent in root.xpath('//*[./*]'):
    parent[:] = sorted(parent, key=lambda x: x.tag)

# The child elements of the root are already ordered by tag. Now order each
# element with the same tag (e.g., script-group, job-config, etc) by ID.
element_list = []

for elem in root.iterchildren():
    tmp_tag = elem.tag
    tmp_attr = int(elem.attrib.get('id'))
    elem_str = etree.tostring(elem)
    element_list.append((tmp_tag, tmp_attr, elem_str))

# Get things in sorted order, then print only the last part of the tuple with
# the XML string. key=itemgetter() does a two-level sort, first by element
# name, and then by id. decode() produces raw ASCII from a binary string.
for elem_str in sorted(element_list, key=itemgetter(0, 1)):
    print(elem_str[2].decode('ascii'))

