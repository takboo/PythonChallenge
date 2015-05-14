#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://www.pythonchallenge.com/pc/def/bull.html

def calcnext(current):

    curlen = len(current)
    i = 0

    next = ''
    count = 1
    for i in range(0,curlen):
        if i+1 != curlen and current[i] == current[i+1]:
            count += 1
        else:
            next += str(count)
            next += str(current[i])
            count = 1


    return next

if __name__ == "__main__":
    a = ['1']

    for i in range(0,31):
        Temp = calcnext(a[i])
        a.append(Temp)

    print(len(a[30]))


