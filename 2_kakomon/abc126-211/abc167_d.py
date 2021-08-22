from math import log2

n,k = map(int, input().split())
al = list(map(int, input().split()))

logk = int(log2(k))+1
db = [ [0]*n for _ in range(logk) ]
for ni in range(n): 
    db[0][ni] = al[ni]-1
for ki in range(logk-1):
    for ni in range(n):
        db[ki+1][ni] = db[ki][db[ki][ni]]

now = 0
for i in range(logk):
    if k&(1<<i) > 0:
        now = db[i][now]
print(now+1)

