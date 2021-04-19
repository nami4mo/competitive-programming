import sys
input = sys.stdin.readline

al=[]
from collections import deque
for _ in range(int(input())):
    n=int(input())
    s=input().rstrip()
    tq=deque()
    ms=[]
    for i,si in enumerate(s):
        if si=='T':tq.append(i)
        else:ms.append(i)

    # print(tq,ms)
    if len(tq)!=len(ms)*2:
        al.append('NO')
        continue

    ok=True
    for mi in ms:
        if tq and tq[0]<mi:
            tq.popleft()
        else:
            ok=False
            break
        
    for mi in ms[::-1]:
        if tq and mi<tq[-1]:
            tq.pop()
        else:
            ok=False
            break  
    
    if ok: al.append('YES')
    else:al.append('NO')

for a in al:print(a)