from datetime import datetime
a = datetime.now()


score = {'':0, 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, '#':0}
rscore = dict((a,b) for b,a in score.items())


with open('p022_names.txt', 'r') as f:
    lines = f.readline()

line = '",' + lines + ',"'


alist = line.split('","')
alist.sort()

alist.remove('')
print alist[-1]
print alist[0:3]
print alist.index('COLIN')

lena = len(alist)
i = 1
d = 0

while i < lena:
    if i == lena-1:
        print alist[i]
        print alist[-1]
##    if i == 938:
##        print alist[i]
##        k = 0
##        for x in alist[i]:
##            k += score[x.upper()]
##        print k
##        print k*i
    n = 0
    name = alist[i]
    for letter in name:
        n += score[letter.upper()]
    n *= i
    d += n
    i += 1
    
    
print d




b = datetime.now()
print b - a
