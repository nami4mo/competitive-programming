n,m=map(int, input().split())
gl=[[] for _ in range(n)]
cds={}
for _ in range(m):
    a,b,c=map(str, input().split())
    a,b=int(a)-1,int(b)-1
    gl[a].append((b,c))
    gl[b].append((a,c))

from collections import deque
fq=deque()
fq.append((0,(n-1,),0))

used=[[0]*(n) for _ in range(n)]
used[0][n-1]=1

ans=10**10
ok=False
while fq:
    break_flag=False
    fpoped, bpopeds, dist=fq.popleft()
    for neib,c in gl[fpoped]:
        if neib in bpopeds and neib!=fpoped:
            break_flag=True
            ok=True
            ans=min(ans,dist*2+1)
        new_b=[]
        for bpoped in bpopeds:
            for bneib, bc in gl[bpoped]:
                if neib==bneib and c==bc:
                    break_flag=True
                    ans=min(ans,dist*2+2)
                    ok=True
                    break
                if c==bc and used[neib][bneib]<1: 
                    new_b.append(bneib)
                    used[neib][bneib]+=1
            if new_b and not ok:
                fq.append((neib, new_b, dist+1))

if ans==10**10:ans=-1
print(ans)