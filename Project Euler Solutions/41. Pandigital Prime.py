from datetime import datetime

at=datetime.now()

import itertools
x = '987654321'

def check_if_prime(num):
    num = int(num)
    for j in xrange(2, int(num**0.5+1)):
        if num%j == 0:
            return False
    return True

perm = [''.join(p) for p in itertools.permutations(x)]
while len(x)>0:
    for i in perm:
        if check_if_prime(i):
            print i
            break
    x = x[1:]
    perm = [''.join(p) for p in itertools.permutations(x)]

bt=datetime.now()
print bt-at

