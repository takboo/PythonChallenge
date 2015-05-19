#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://www.pythonchallenge.com/pc/def/peak.html

#序列化
import cPickle as Pickele
from __builtin__ import file

if __name__ == "__main__":

    with open('banner.p','r') as F:
        strorelist = Pickele.load(F)

        print(strorelist)

        for row in strorelist:
            temp = ''
            for line in row:
                temp += line[0] * line[1]
            print(temp)

