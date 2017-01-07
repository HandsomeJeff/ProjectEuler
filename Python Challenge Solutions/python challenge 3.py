import urllib2
first=94485
second=16044
sec=second/2
third=63579

dog=60074

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % third

response = urllib2.urlopen(url)
html = response.read()
x=1
while True:
    if x<400:
        inp = str(html)
        dog = int(inp[24:])
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % dog
        response = urllib2.urlopen(url)
        html = response.read()
        if str(html)[:3] ==  'and':
            print html
        else:
            print html
            break
        x+=1


