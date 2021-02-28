def fail():
    print(0)
    exit()

n,m=map(int, input().split())
gl=[[]*n for _ in range(n)]
for _ in range(m):
    u,v,s=map(int, input().split())
    u-=1
    v-=1
    gl[u].append((v,s))
    gl[v].append((u,s))

vals=[(0,0)]*n
from collections import deque
q=deque([0])
vals[0]=(1,0)

aval=None
while q:
    poped=q.popleft()
    ai,vi=vals[poped]
    # print(vals)
    for neib,s in gl[poped]:
        if vals[neib][0]!=0:
            ai2,vi2=vals[neib]
            if ai!=ai2:
                if vi+vi2!=s:fail()
                else:continue
            if ai==ai2 and ai==1:
                a2=s-(vi+vi2)
                if a2%2!=0:fail()
                c_aval=a2//2
            elif ai==ai2 and ai==-1:
                a2=(vi+vi2)-s
                if a2%2!=0:fail()
                c_aval=a2//2
            if aval is None:
                if c_aval>0:aval=c_aval
                else:fail()
            else:
                if aval!=c_aval:fail()
        else:
            aai=(-1)*ai
            vvi=s-vi
            vals[neib]=(aai,vvi)
            q.append(neib)

if aval is not None:
    for a,v in vals:
        val=a*aval+v
        if val<=0:fail()
    else:
        print(1)
    exit()

amin=1
amax=10**10
for a,v in vals:
    if a==-1:
        amax=min(amax,v-1)
    else:
        amin=max(amin,(-1)*v+1)

ans=amax-amin+1
ans=max(0,ans)
print(ans)