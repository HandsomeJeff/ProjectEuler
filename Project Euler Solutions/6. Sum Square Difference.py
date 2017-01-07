def smsq(x):
    i=1
    n=0
    while i <= x:
        n += (i**2)
        i += 1
    p=1
    q=0
    while p <= x:
        q += p
        p += 1
    print abs(n - q**2)

from datetime import datetime
a = datetime.now()
smsq(100)
b = datetime.now()
print b-a
