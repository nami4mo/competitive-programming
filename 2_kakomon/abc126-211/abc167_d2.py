from math import log2
n,k=map(int, input().split())
al=list(map(int, input().split()))

logk=int(log2(k))+1

db=[[0]*n for _ in range(logk)]
for i in range(n):
    db[0][i]=al[i]-1
for ki in range(logk-1):
    for i in range(n):
        db[ki+1][i]=db[ki][db[ki][i]]
pos=0
for i in range(logk):
    if k&(1<<i)>0: pos=db[i][pos]
print(pos+1)