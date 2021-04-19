n=int(input())
from collections import deque

al=[]
for _ in range(n):
    row=list(map(int, input().split()))
    row=[v-1 for v in row]
    al.append(deque(row))


cand=list(range(n))
cnt=0
ans=0
while True:
    new_cand=[]
    update=False
    ans+=1
    used=set()
    for c in cand:
        if not al[c] or c in used:continue
        aite=al[c][0]
        if al[aite] and al[aite][0]==c and (not aite in used):
            cnt+=1
            al[c].popleft()
            al[aite].popleft()
            used.add(c)
            used.add(aite)
            new_cand.append(c)
            new_cand.append(aite)
            update=True
    cand=new_cand[:]
    if cnt==n*(n-1)//2:
        break
    if not update:
        ans=-1
        break
print(ans)