from bisect import bisect_left, bisect_right
from collections import deque
import sys
input = sys.stdin.readline

n,k=map(int, input().split())
abl=[]
for _ in range(n):
    a,b=map(int, input().split())
    abl.append((a,b))
abl.sort()
al=[]
bl=[]
for a,b in abl:
    al.append(a)
    bl.append(b)

MAX=5001
pos=[[] for _ in range(MAX)]
for i in range(n):
    b=bl[i]
    pos[b].append(i)

posl=[0]*MAX
posr=[0]*MAX
ans=0
for u in range(MAX):
    left = bisect_left(al, u)
    if not 0<=left<n:continue
    right = bisect_right(al, u+k)-1
    if left>right:continue
    q=deque()
    val=0
    for v in range(MAX):
        while posr[v]<len(pos[v]) and pos[v][posr[v]]<=right:
            posr[v]+=1
        while posl[v]<len(pos[v]) and pos[v][posl[v]]<left:
            posl[v]+=1
        if not pos[v]:
            vcnt=0
        elif right<pos[v][0]:
            vcnt=0
        else:
            vcnt=posr[v]-posl[v]
        val+=vcnt
        q.append(vcnt)
        if len(q)>k+1:
            val-=q.popleft()
        ans=max(ans,val)
print(ans)