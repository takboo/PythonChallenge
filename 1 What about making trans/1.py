#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://www.pythonchallenge.com/pc/def/map.html
'python challenge Level 1'

def my_mktrans(str1,str2):
    if len(str1) != len(str2):
        raise IndexError
    retmap = {} 
    i = 0
    while i < len(str1):
        retmap[str1[i]] = str2[i]
        i += 1
    return retmap

def my_translate(source,my_map):
    retstr = ""
    i = 0
    while i < len(source):
        Temp = my_map.get(source[i])
        if Temp == None:
            retstr += source[i]
        else:
            retstr += Temp
        i += 1
    return retstr


OriginalMap = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

NewMap      = "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB"

EncodeStr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#string.maketrans will only works on Py2
#map = string.maketrans(OriginalMap,NewMap)

my_map = my_mktrans(OriginalMap,NewMap)

Temp = my_translate(EncodeStr,my_map)
print(Temp)

url = "map"

print(".....apply the url......")
print("map = " + my_translate(url,my_map))
