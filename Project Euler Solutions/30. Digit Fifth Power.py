from datetime import datetime

at=datetime.now()


alist=[]

d=0
x=2
#max number is 6 digits (9**5)*7 = 6 digits
while x<354294:
    p=0
    for n in str(x):
        p+=(int(n)**5)
    if p==x:
        d+=x
    x+=1
print d




bt=datetime.now()

print bt-at



