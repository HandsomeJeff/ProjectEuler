from datetime import datetime
at=datetime.now()

x=1
alist=[]


while x<200000:
    alist.append(str(x))
    x+=1

s=(''.join(alist))
blist=[0]
x=9
while x<1000000:
    blist.append(x)
    x=x*10+9

d=1
for x in blist:
    d=d*int(s[x])


print d

bt=datetime.now()
print bt-at
