from datetime import datetime
a=datetime.now()

def f(n):
    i=1
    while int(n)!=1:
        if n%2==0:
            n=n/2
            i+=1
        else:
            n=3*n+1
            i+=1

    return i

x=500001
alist=[]
while x<1000000:
    alist.append(f(x))
    x+=2
dog=max(alist)
x=999999
while x>500001:
    if f(x)!=dog:
        x-=2
    elif f(x) == dog:
        print x
        break


b=datetime.now()
print b-a


