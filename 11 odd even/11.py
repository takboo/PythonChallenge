# !/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.pythonchallenge.com/pc/return/5808.html


from PIL import Image

if __name__ == "__main__":
    a = Image.open('cave.jpg')
    b = Image.new(a.mode, a.size)
    aPixels = a.load()
    bPixels = b.load()
    for i in range(a.size[0]):
        for j in range(a.size[1]):
            if i % 2 == j % 2:
                b.putpixel((i, j), a.getpixel((i, j)))
    b.show()
