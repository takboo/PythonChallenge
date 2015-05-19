#! /usr/bin/env python
'''python challenge level 14
question url: http://www.pythonchallenge.com/pc/return/italy.html
answer url: http://www.pythonchallenge.com/pc/return/uzi.html
'''

l = [[i, i - 1 , i - 1, i - 2] for i in xrange(100, 1, -2)]
l = reduce(lambda x, y: x+y, l)
# print l, len(l)

from PIL import Image
org = Image.open('wire.png')
org_data = list(org.getdata())
res = Image.new(org.mode, (100, 100))
res_data = res.load()

# (0,0)
#    ---->x
#    |
#    vy
dire = [(1, 0),(0, 1),(-1, 0),(0, -1)]

# init
v = 0
org_index = 0
res_pos = (-1, 0)
for times in l:
    for i in xrange(times):
        # pos will out of index if reset position after setting color
        res_pos = tuple(map(lambda x, y: x + y, res_pos, dire[v]))
        res_data[res_pos] = org_data[org_index]
        org_index += 1
    v = (v + 1) % 4

res.save("answer.png")