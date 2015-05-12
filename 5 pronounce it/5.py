#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://www.pythonchallenge.com/pc/def/peak.html

#序列化
import cPickle as Pickele
from __builtin__ import file

f = file('banner.p','r')

strorelist = Pickele.load(f)

for i in strorelist:
    TempStr = ''
    for j in i:
        TempStr += j[0] * j[1]
    print TempStr

