from datetime import datetime

at=datetime.now()

import itertools


def check_if_prime(num):
    num = int(num)
    for j in xrange(2, int(num**0.5+1)):
        if num%j == 0:
            return False
    return True


alist =[2]
i = 3
while i<10000:
    if check_if_prime(i):
        alist.append(i)        
    i+=2


x=len(alist)-1
p=0
blist = []
maxl = 20
while p<len(alist):
    x=len(alist)-1
    while x-p>maxl:
        d = sum(alist[p:p+x])
        l = len(alist[p:p+x])
        if check_if_prime(d) and d<1000000:
            if l>maxl:
                maxl = l
                blist.append(d)
                blist.append(l)
        x-=1
        print blist
    p+=1
    print blist
    if d == 0:
        break


bt=datetime.now()
print bt-at

