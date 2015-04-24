#http://www.pythonchallenge.com/pc/def/map.html

import string

OriginalMap = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

NewMap      = "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB"

EncodeStr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

map = string.maketrans(OriginalMap,NewMap)

print(EncodeStr.translate(map))

url = "map"

print(".....apply the url......")
print("map = " + url.translate(map))
