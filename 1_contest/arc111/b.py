MAX=400001
n=int(input())
pairs=[[] for _ in range(MAX)]
cnts=[0]*MAX
for _ in range(n):
    a,b=map(int, input().split())
    cnts[a]+=1
    cnts[b]+=1
    pairs[a].append(b)
    pairs[b].append(a)

from collections import deque
onesq=deque()
ans=0
for num in range(MAX):
    if cnts[num]==1:
        onesq.append(num)

while onesq:
    poped=onesq.popleft()
    if cnts[poped]<1:continue
    ans+=1
    for pair in pairs[poped]:
        cnts[pair]-=1
        if cnts[pair]==1:onesq.append(pair)

for num in range(MAX):
    if cnts[num]>=2:
        ans+=1

print(ans)