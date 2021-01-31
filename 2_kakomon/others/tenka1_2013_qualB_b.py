Q,l=map(int, input().split())
from collections import deque
q=deque()
cnt=0

ansl=[]
end='SAFE'
for _ in range(Q):
    qu=list(input().split())
    if qu[0]=='Push':
        n,m=int(qu[1]),int(qu[2])
        q.append((m,n))
        cnt+=n
        if cnt>l:
            end='FULL'
            break
    elif qu[0]=='Pop':
        n=int(qu[1])
        if cnt<n:
            end='EMPTY'
            ok=False
            break
        cnt-=n
        while n>0:
            # print(n)
            if q[-1][1]<=n:
                n-=q[-1][1]
                q.pop()
            else:
                q[-1]=(q[-1][0],q[-1][1]-n)
                break
    elif qu[0]=='Top':
        if cnt==0:
            end='EMPTY'
            ok=False
            break
        ansl.append(q[-1][0])
    else:
        ansl.append(cnt)

for a in ansl:print(a)
print(end)