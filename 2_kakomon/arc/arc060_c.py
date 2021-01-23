from bisect import bisect_left, bisect_right

n=int(input())
xl=list(map(int, input().split()))
l=int(input())
q=int(input())
nexts=[-1]*n
for i in range(n):
    v=bisect_right(xl,xl[i]+l)-1
    nexts[i]=v
# print(nexts)

from math import log2
logn = int(log2(n))+2
db=[[0]*n for _ in range(logn)]
for i in range(n):
    db[0][i]=nexts[i]

for i in range(logn-1):
    for j in range(n):
        db[i+1][j] = db[i][db[i][j]]

# print(db)
ansl=[]
for _ in range(q):
    a,b=map(int, input().split())
    if a>b:a,b=b,a
    a-=1
    b-=1
    dist=0
    curr=a
    for i in range(logn-1,-1,-1):
        if db[i][curr]<b:
            curr=db[i][curr]
            dist+=pow(2,i)
    if curr<b:dist+=1
    ansl.append(dist)

for a in ansl:print(a)
