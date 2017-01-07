from datetime import datetime
a=datetime.now()


def p(x):
    if x == x[::-1]:
        return True

i=1
d=0
while i<1000000:
    si=str(i)
    
    if si==si[::-1] and bin(i)[2:]==bin(i)[2:][::-1]:
        d+=i
    i+=1
print d



b=datetime.now()
print b-a


