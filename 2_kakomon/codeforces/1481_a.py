al=[]
from collections import Counter
for _ in range(int(input())):
    x,y=map(int, input().split())
    s=input()
    c=Counter(s)
    xma,xmi=c['R'],-c['L']
    yma,ymi=c['U'],-c['D']
    if xmi<=x<=xma and ymi<=y<=yma:
        al.append('YES')
    else:
        al.append('NO')
for a in al:print(a)