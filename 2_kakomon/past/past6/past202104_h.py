n,m,k,q=map(int, input().split())
kan=[]
freekan=[]
for _ in range(n):
    p,t=map(int, input().split())
    if t==0:
        freekan.append(p)
    else:
        kan.append(p)

kan.sort()
freekan.sort()
from collections import deque
# kanq=deque(kan)
# freekanq=deque(freekan)
ans=10**18
csum=0
kiri=0
kirival=0
if len(freekan)>=m:
    freekanq=deque(freekan[:m])
    kanq=deque(kan)
    csum=sum(freekan[:m])
    ans=csum
else:
    freekanq=deque(freekan)
    csum=sum(freekan)
    rem=m-len(freekan)
    csum+=sum(kan[:rem])
    kanq=deque(kan[rem:])
    kiri+=rem
    kirival=((kiri-1)//k+1)*q
    # kiri%=k
    
ans=min(ans, csum+kirival)

# print(kanq,freekanq,kirival)
while kanq and freekanq:
    # if kanq[0]<freekanq[-1]:
    kiri+=1
    kirival=((kiri-1)//k+1)*q
    diff=freekanq.pop()-kanq.popleft()
    csum-=diff
    ans=min(ans, csum+kirival)
    # else:
    #     break
print(ans)