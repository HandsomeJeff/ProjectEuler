from datetime import datetime
a=datetime.now()

numdict = { 0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
tendict = { 0:3, 1:6, 2:6, 3:8, 4:8, 5:7, 6:7, 7:9, 8:8, 9:8}
tensdict = { 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}

i = 1
d = 0

while i < 1000:
    j = d
    si = str(i)
    if i % 100 == 0:
        k = i//100
        if k <10:
            d += len('hundred')
            d += numdict[k]
    else:
        if len(si) > 1 and si[-2] == '1':
            d += tendict[int(si[-1])]
        else:
            d += numdict[int(si[-1])]
            if len(si) > 1:
                if si[-2] != '0':
                    d += tensdict[int(si[-2])]
        if i > 100:
            k = i//100
            if k <10:
                d += len('hundredand')
                d += numdict[k]

##    for testing
##    print 'i=%s, d=%s' % (i,d)
##    print 'difference=%s' % (d-j)
    
    i += 1

d += len('onethousand')
print d


b=datetime.now()
print b-a
