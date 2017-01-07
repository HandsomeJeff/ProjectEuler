import urllib2
import pickle


url = "http://www.pythonchallenge.com/pc/def/peak.html"

dog = pickle.load(open("banner.p"))

d=''
for x in dog:
    for a in x:
        d+=a[0]*a[1]
print d



