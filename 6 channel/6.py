#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://www.pythonchallenge.com/pc/def/channel.html

import zipfile
import re

#获取起始的数字
def GetBeginNothing(filename):
    with zipfile.ZipFile(filename,'r') as zFile:
        namelist = zFile.namelist()

        for name in namelist:
            if name == 'readme.txt':
                content = zFile.read(name)
                pattern = re.compile(r'\d{2,}')
                nextnum = pattern.findall(content)
                return nextnum[0]

def FindExit(filename,next):
    with zipfile.ZipFile(filename,'r') as zFile:
        namelist = zFile.namelist()

        n = len(namelist) - 1
        comment = ''
        while(n):
            next = next + '.txt'
            if next in namelist:
                content = zFile.read(next)
                comment += zFile.getinfo(next).comment
                print(content)
                pattern = re.compile(r'\d{2,}')
                nextnum = pattern.findall(content)
                if nextnum:
                    next = nextnum[0]
                n = n -1
    return comment


if __name__ == '__main__':
    filename = 'channel.zip'
    nextnum = GetBeginNothing(filename)
    comment = FindExit(filename,nextnum)
    print(comment)





