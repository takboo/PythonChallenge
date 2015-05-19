#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.pythonchallenge.com/pc/def/map.html

import string

if __name__ == "__main__":

    original = string.ascii_lowercase
    trans = original[2:] + original[:2]

    EncodeStr = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgag"
                 "clr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc sp"
                 "j.")

    transtab = string.maketrans(original, trans)

    Temp = string.translate(EncodeStr.lower(), transtab)
    print(Temp)

    url = "map"

    print(".....apply the url......")
    print("map = " + string.translate(url, transtab))
