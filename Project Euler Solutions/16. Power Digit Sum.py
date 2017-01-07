from datetime import datetime
a=datetime.now()

x=2**1000
sx=str(x)
alist=[]
for n in range(len(sx)):
    alist.append(int(sx[n]))

print sum(alist)

b=datetime.now()
print b-a



a=datetime.now()

sum = 0
for n in str(2**1000):
	sum += int(n)
print sum

b=datetime.now()
print b-a
