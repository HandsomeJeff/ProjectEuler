
def smmul(p):
    alist = []

    alist.append(2)
    alist.append(3)
    for i in range(3,p+1,2):
        n=3

        while n < i:
            if i%n == 0:
                break
            else:
                alist.append(i)
                break
            n+=2

    for x in reversed(alist):
        for y in alist:
            if x>y and x%y==0:
                alist.remove(x)
                break

    d=alist[10000]

    print d

from datetime import datetime
a = datetime.now()
smmul(110000)
b = datetime.now()
print b-a


