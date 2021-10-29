def m3(v,keta):
    res=[]
    for _ in range(keta):
        res.append(str(v%3))
        v//=3
    return res

n,l=map(int, input().split())

keta=0
for i in range(20):
    if pow(3,i)>=n:
        keta=i
        break

al=[]
bl=[]
cl=[]
for i in range(n):
    a=m3(i,keta)
    b=[]
    for v in a:
        if v=='0':b.append('1')
        if v=='1':b.append('2')
        if v=='2':b.append('0')
    c=[]
    for v in b:
        if v=='0':c.append('1')
        if v=='1':c.append('2')
        if v=='2':c.append('0')
    rem=l-keta-1
    a.extend(['0']*rem)
    b.extend(['1']*rem)
    c.extend(['2']*rem)
    a.append('2')
    b.append('1')
    c.append('0')
    print(''.join(a[::-1]))
    print(''.join(b[::-1]))
    print(''.join(c[::-1]))