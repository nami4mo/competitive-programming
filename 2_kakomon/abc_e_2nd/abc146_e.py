n,k=map(int, input().split())
al=list(map(int, input().split()))

from collections import deque
# cnts=[0]*k
cnts={}
cnts[0]=1
q=deque([(0,0)])

ans=0
csum=0
for i,a in enumerate(al):
    ind=i+1
    if q and q[0][0]==(ind-k):
        _,v=q.popleft()
        cnts[v]-=1
    csum+=a
    csum%=k
    val=(csum-ind)%k
    cnts.setdefault(val,0)
    ans+=cnts[val]
    q.append((ind,val))
    cnts[val]+=1
print(ans)