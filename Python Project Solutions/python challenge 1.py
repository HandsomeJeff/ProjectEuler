from datetime import datetime
a=datetime.now()
dog = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, ' ':0, "'":27, '(': 28, ')': 29, '.':30, '/':31, ':':32}
rdog = dict((a,b) for b,a in dog.items())

ind = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
inp = ind.upper()
alist = []
blist = []
x=0
while x < len(inp):
    alist.append(inp[x])
    x+=1

for i in alist:
    blist.append(dog[i])
clist = []
i=0
while i<len(blist):
    for n in range(27):
        if blist[i] == 0:
            clist.append(rdog[0])
            break
        elif blist[i] == n and blist[i] !=0 and blist != 25 and blist != 26:
            clist.append(rdog[n+2])
            break
        elif blist[i] == 25:
            clist.append(rdog[1])
            break
        elif blist[i] == 26:
            clist.append(rdog[2])
            break
        elif blist[i] >= 27:
            clist.append(rdog[blist[i]])
            break
    i+=1

print ''.join(clist).lower()

b=datetime.now()
print b-a


a=datetime.now()

from string import maketrans
inp = 'abcdefghijklmnopqrstuvwxyz'
outp = 'cdefghijklmnopqrstuvwxyzab'

ind = """mapg fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
print ind.translate(maketrans(inp, outp))



b=datetime.now()
print b-a
