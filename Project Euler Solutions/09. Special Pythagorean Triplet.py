from datetime import datetime
x=datetime.now()
for a in range(1,1000):
    for b in range(1000,1,-1):
        c = (((a**2)+(b**2))**0.5 )
        if float(c)==float(int(c)):
            if c+a+b==1000:
                print a*b*c

y=datetime.now()
print y-x
