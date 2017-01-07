
from datetime import datetime

a=datetime.now()


def am(x):
    d = 0
    i = 1
    while i < x:
        if x % i == 0:
            d += i
        i += 1
    return d

d = 0
i = 1
while i < 10000:
    ai = am(i)
    if ai != i and am(ai) == i:
        d += i
        print i
    i += 1

print d




b=datetime.now()
print b-a
