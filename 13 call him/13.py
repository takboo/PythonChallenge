# !usr/bin/env python
# _*_ coding: utf-8 _*_
# http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpclib

if __name__ == "__main__":
    remote = xmlrpclib.Server("http://www.pythonchallenge.com/pc/phonebook.php")
    print(remote.system.listMethods())

    print(remote.phone("xxx"))
    print(remote.phone("Bert"))