
def smmul(p):
    alist = [2,3]
    append=alist.append
    remove=alist.remove
    for i in range(3,p+1,2):
        n=3

        while n < i:
            if i%n == 0:
                break
            else:
                append(i)
                break
            n+=2

    for x in reversed(alist):
        for y in alist:
            if x>y and x%y==0:
                remove(x)
                break

    print alist
    d=1
    for x in alist:
        n=1
        while x**n < p:
            if x**(n+1) > p:
                d*=(x**n)
                break
            else:
                n+=1

    print d

from datetime import datetime
a = datetime.now()
smmul(20)
b = datetime.now()
print b-a

a = datetime.now()
prime_list = [2]
check_num = 3
i = 0
while len(prime_list) < 10001:
    if prime_list[i]**2 > check_num:
        prime_list.append(check_num)
        i = 0
        check_num += 1
    elif check_num % prime_list[i] == 0:
        i = 0
        check_num += 1
    else:
        i += 1

print prime_list[10000]
b = datetime.now()
print b-a
