# !usr/bin/env python
# _*_ coding: utf-8 _*_
# http://www.pythonchallenge.com/pc/return/evil.html

if __name__ == "__main__":

    with open('evil2.gfx','rb') as evilfile:
        evildata = evilfile.read(-1)
        for i in range(5):
            with open('evil_%d.jpg'%i,'wb') as sliptevil:
                sliptevil.write(evildata[i::5])

