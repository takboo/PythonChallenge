#!/usr/bin/env python
#-*- coding: utf-8 -*-
#http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image

if __name__ == '__main__':

    im = Image.open('oxygen.png')

    #构建box 获取灰色区域图像
    box = (0,43,im.size[0],52)
    gray = im.crop(box)
    gray.show()
    gray = gray.convert('L')
    msg = gray.tostring()
    print(msg)

    #获取正确提示
    print(msg[4:610:7])

    tip = [105, 110, 116, 101, 103, 114, 105, 116, 121]

    nextlevel = ''
    #获取通关信息
    for i in tip:
       nextlevel += chr(i)

    print(nextlevel)

