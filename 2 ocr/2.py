#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://www.pythonchallenge.com/pc/def/ocr.html
import re

with open('MessData.txt','r') as F:
  mess = F.read(-1)
  pattern = re.compile('[a-zA-Z]+')
  match = pattern.findall(mess)
  print(''.join(match))
