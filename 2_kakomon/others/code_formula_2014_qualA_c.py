n,k=map(int, input().split())
rem=k

al=[]
for _ in range(n):
    row=list(map(int, input().split()))
    al.append(row)

used=[False]*(10**6)
from collections import deque
waits=[deque() for _ in range(k+1)]

for i, row in enumerate(al):
    rem_yosen=n-(i+1)
    for j in range(k):
        a=row[j]
        if not used[a]: waits[j].append(a)
    # while True:
    ansl=[]
    for c in range(k):
        while waits[c] and c*rem_yosen<rem:
            poped=waits[c].popleft()
            if used[poped]: continue
            used[poped]=True
            ansl.append(poped)
            rem-=1
    ansl.sort()
    print(*ansl)
