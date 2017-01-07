from datetime import datetime

at=datetime.now()

from math import factorial
alist=[]

d=0
x=3
#max number is 7 digits (9!)*8 = 7 digits
while x<50000:
    p=0
    for n in str(x):
        p+=(factorial(int(n)))
    if p==x:
        d+=x
        print x
    x+=1
print d




bt=datetime.now()

print bt-at



