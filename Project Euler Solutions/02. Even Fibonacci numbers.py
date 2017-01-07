def fb(x):
    alist=[1,1]
    i=2
    while i<x:
        alist.append(alist[i-2]+alist[i-1])
        i+=1
    return alist[i-1]
print fb(5000)
    
    
from datetime import datetime

a=datetime.now()
i=0
x=1
while fb(x)<=4000000:
    if fb(x)%2==0:
        i+=fb(x)
    x+=1

print i
b=datetime.now()
print b-a

a=datetime.now()
i=0
x=1
while True:
    if fb(x)<=4000000 and fb(x)%2==0:
        i+=fb(x)

    x+=1


print i
b=datetime.now()
print b-a
