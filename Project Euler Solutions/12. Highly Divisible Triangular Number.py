from datetime import datetime
a=datetime.now()

alist = [1,3,6]

i = 4
while i < 20000:
    alist.append(alist[-1]+i)
    i+=1

def f(x):
    d=0
    i=1
    while i<x**.5:
        if x%i==0:
            d+=2
        i+=1
    return d


for x in alist:
    if f(x)>500:
        print x
        break


b=datetime.now()
print b-a
