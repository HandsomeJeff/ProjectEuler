from datetime import datetime
a=datetime.now()


dog = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, '#':0}

with open('42. Coded Triangle Numbers.txt','r') as text:
    ad = text.read()
ad = ad.replace('"',"")
alist = ad.split(',')

def tri(x):
    x = x.upper()
    d=0
    for i in x:
        d+=dog[i]
    return d

def ntri(x):
    alist=[]
    i=1
    while i<x+1:
        alist.append(i*(i+1)/2)
        i+=1
    return alist

ntr = ntri(len(alist))
i=0
for x in alist:
    tx = tri(x)
    if tx in ntr:
        i+=1
print i
    

b=datetime.now()
print b-a


