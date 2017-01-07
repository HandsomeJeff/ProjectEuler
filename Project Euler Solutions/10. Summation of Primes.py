from datetime import datetime

#variant1
at=datetime.now()

n = 17
i = 3
alist = [2,3,5,7,11,13,17]
for x in range(3, 100000, 2):
    while i < int(x**.5)+1:
        if x % i ==0 or x % (i+2) == 0 or x % (i+4) == 0 or x % (i+6) == 0 or x % (i+8) ==0 or x % (i+10) == 0 or x % (i+12) == 0 or x % (i+14) == 0:
            break
        else:
            alist.append(x)
            break
        i+=2


slist = sum(alist)
blist = alist[0:len(alist)/17]
s=set(alist)

for a in s:
    for b in blist:
        if a>b and a%b==0:
            slist -= a
            break


print slist

bt=datetime.now()
print bt-at

#variant2
at=datetime.now()
sum = 2
def check_if_prime(num):
    for j in xrange(2, int(num**0.5+1)):
        if num%j == 0:
            return False
    return True
for i in xrange(3, 100000, 2):
    if check_if_prime(i):
        sum += i
print sum
bt=datetime.now()

print bt-at

