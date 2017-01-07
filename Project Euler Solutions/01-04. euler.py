#1
def m35(p):
    mlist = []
    for x in range(1,p):
        if x%3==0 or x%5==0:
            mlist.append(x)
        elif x%15==0:
            mlist.append(-int(x))
    print sum(mlist)

inp = int(raw_input())
for x in range(1,1000):
    if 3**x==inp:
        print True
        print x



def fb(x):
    if x<=1:
        return x
    if x>1:
        return fb(x-2)+fb(x-1)

def p(x):
    elist = []
    if x%2==0:
        x/=2
        elist.append(2)
    i=3
    while x>=i*i:
        while x%i==0:
            x/=i
            elist.append(i)
        i+=2
    if x>1:
        elist.append(x)
    return elist[len(elist)-1]

def pal(p):
    flist = []
    for x in range(100,p):
        if x%11==0:
            for y in range(100,p):
                xy = x*y
                if str(xy)==str(xy)[::-1]:
                    flist.append(xy)
    print max(flist)

def factorial(x):
    for i in range(1,x,1):
        x *= i
    return x

def prime(x):
    for i in range(2,x/2+1):
        if x%i != 0:
            return True
        elif x%i ==0:
            return False

x=1
for i in range(3,11,2):
    for n in range(2, 0, -1):
        if 10 >= (i^n) and (i^n) > 10/2:
            x*= (i^n)
print x



        


