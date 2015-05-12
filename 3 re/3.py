#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://www.pythonchallenge.com/pc/def/equality.html

import re

with open('ReData.txt','r') as F:
  Text = F.read()
  #零宽断言 ?=匹配之前的 ?<= 匹配之后
  findTable = re.findall(r'(?<=[a-z]{1}[A-Z]{3})[a-z]{1}(?=[A-Z]{3}[a-z]{1})',Text)
  print(''.join(findTable))
