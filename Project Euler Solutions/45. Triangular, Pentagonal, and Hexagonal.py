from datetime import datetime
at=datetime.now()

def p(x):
    return x*(3*x-1)/2
def h(x):
    return x*(2*x-1)

blist=[]
clist=[]

x=100
end = 1000

while x<end:
    clist.append(h(x))
    blist.append(p(x))
    x+=1

d=0
for a in clist:
    if a in blist:
        print a
        

bt=datetime.now()
print bt-at

at=datetime.now()

def p(x):
    return x*(3*x-1)/2
def h(x):
    return x*(2*x-1)
blist=[]
clist=[]
x=100
end = 40000

while x<end:
    clist.append(h(x))
    blist.append(p(x))
    x+=1


h=set(clist)
p=set(blist)
print(p.intersection(h))

bt=datetime.now()
print bt-at


