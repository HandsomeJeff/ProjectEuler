from datetime import datetime

at=datetime.now()

def prime(x):
    if x % 2 == 0:
        return False
    i = 3
    while i <= x/2+1:
        if x%i == 0:
            return False
        i+=2
    return True

plist = []
for x in range(1000,9999):
    if prime(x):
        plist.append(x)

lenp = len(plist)
x = 0
while x < lenp:
    a = str(plist[x])
    alist = [y for y in a]
    alist.sort()
    i = x + 1
    difference = (lenp - x)/2+1
    diffx = x + difference
    while i < diffx:
        b = str(plist[i])
        blist = [y for y in b]
        blist.sort()
        if alist == blist:
            n = i + 1
            diffi = i + difference
            while n < diffi:
                c = str(plist[n-1])
                clist = [y for y in c]
                clist.sort()
                if int(c) - int(b) == int(b) - int(a) and blist == clist:
                    print a,b,c
                n += 1
        i += 1
    x += 1

bt=datetime.now()
print bt-at




x = 1487
#less efficient
while x <= 9999:
    break
    if prime(x):
        a = str(x)
        alist = [i for i in a]
        alist.sort()
        if len(alist) == 4:
            i = x+2
            difference = (9999-x)/2
            diffx = x + difference
            while i <= diffx:
                if prime(i):
                    b = str(i)
                    blist = [n for n in b]
                    blist.sort()
                    if alist == blist:
                        step = i - x
                        n = i + step
                        if prime(n):
                            c = str(n)
                            clist = [p for p in c]
                            clist.sort()
                            if a != b and b!= c and blist == clist:
                                print a+b+c
                                break
                i+=2
    x+=2
            
        



bt=datetime.now()
print bt-at

