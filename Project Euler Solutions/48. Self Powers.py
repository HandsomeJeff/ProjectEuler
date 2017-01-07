from datetime import datetime
a=datetime.now()

i=0
x=1
while x<=1000:
    i+=(x**x)
    x+=1

print str(i)[len(str(i))-10:len(str(i))]

b=datetime.now()

print b-a


a=datetime.now()


print str(sum(x**x for x in range(1,1001)))[-10:]



b=datetime.now()

print b-a
