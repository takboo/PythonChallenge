import urllib2
import re
import string

FirstUrl = "12345"
BaseUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

n = 0
while (n < 400):
  response = urllib2.urlopen(BaseUrl + FirstUrl)
  if(response.read() == "Divide by two and keep going."):
    Div2 = string.atoi(FirstUrl)
    Div2 /= 2
    FirstUrl = '%d'%Div2
    print(FirstUrl)
  else:
    number = re.findall(r'(?<=\s)\d+',response.read())
    print(number)
    FirstUrl = ''.join(number)
    print(FirstUrl)
    n += 1