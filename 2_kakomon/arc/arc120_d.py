n=int(input())
al=list(map(int, input().split()))
al=[(a,i) for i,a in enumerate(al)]
al.sort()
bl=[]
cl=[]
for i in range(n):
    bl.append(al[i][1])
    cl.append(al[i+n][1])

from collections import deque
bq=deque(bl)
cq=deque(cl)
flip=False
cnt=0
ans=[]
for i in range(2*n):
    if bq and bq[0]==i:
        if not flip:
            cnt+=1
            ans.append('(')
        else:
            if cnt==0:
                flip=False
                cnt+=1
                ans.append('(')
            else:
                cnt-=1
                ans.append(')')
        bq.popleft()
    else:
        if flip:
            cnt+=1
            ans.append('(')
        else:
            if cnt==0:
                flip=True
                cnt+=1
                ans.append('(')
            else:
                cnt-=1
                ans.append(')')
        cq.popleft()
print(''.join(ans))