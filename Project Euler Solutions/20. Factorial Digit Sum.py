from datetime import datetime
a=datetime.now()
from math import factorial
x = 100
sx = str(factorial(x))
alist = []
for n in sx:
    alist.append(int(n))
print sum(alist)
b=datetime.now()
print b-a

a=datetime.now()
i=1
n=1
while i<=100:
    n*=i
    i+=1
d=0
for x in str(n):
    d+=int(x)
print d
b=datetime.now()
print b-a


