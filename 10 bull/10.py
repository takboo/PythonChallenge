#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.pythonchallenge.com/pc/def/bull.html


def calcnext(current):

    curlen = len(current)

    mynext = ''
    count = 1
    for i in range(0, curlen):
        if i + 1 != curlen and current[i] == current[i + 1]:
            count += 1
        else:
            mynext += str(count)
            mynext += str(current[i])
            count = 1
    return mynext

if __name__ == "__main__":
    a = ['1']

    for j in range(0, 31):
        Temp = calcnext(a[j])
        a.append(Temp)

    print(len(a[30]))
