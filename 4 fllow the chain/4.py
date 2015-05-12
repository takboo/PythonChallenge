#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://www.pythonchallenge.com/pc/def/linkedlist.html
import urllib2
import re

UrlNum = "12345"
BaseUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

while True:
    print('+--------------------------------------------------+')
    ThisUrl = BaseUrl + UrlNum
    print('URL = %s' %(ThisUrl))
    urlfile = urllib2.urlopen(ThisUrl)
    data = urlfile.read()
    print(data)
    print('+--------------------------------------------------+')
    if 'html' in data:
        print('This is the answer:%s' %('http://www.pythonchallenge.com/pc/def/' + data))
        break
    elif data == 'Yes. Divide by two and keep going.':
        nUrlNum = int(UrlNum)
        nUrlNum /= 2
        UrlNum = str(nUrlNum)
    else:
        if 'There maybe misleading numbers in the \ntext.' in data:
            Found = re.findall(r'\d+',data)
            UrlNum = Found[1]
        else:
            Found = re.findall(r'\d+',data)
            UrlNum = Found[0]
