n,K=map(int, input().split())
MAX=(n-1)*3+1
ds=[0]*MAX

al=list(range(1,n+1))+list(range(n-1,0,-1))
lena=len(al)

cnt=0
csum=0

from collections import deque
q=deque()
for i in range(MAX):
    if i<lena:
        cnt+=1
        a=al[i]
        csum+=a
        q.append(a)
    if i>=lena or cnt>n:
        poped=q.popleft()
        cnt-=1
        csum-=poped
    ds[i]=csum
    
csum=0
vsum=-1
for i in range(MAX):
    if csum+ds[i]>=K:
        vsum=i
        ind=K-csum #1-ind
        break
    csum+=ds[i]

csum=0
for i in range(MAX):
    jk=vsum-i
    if jk>(n-1)*2:continue
    jstart=max(0,jk-n+1)
    kstart=jk-jstart
    cnt=kstart-jstart+1
    if csum+cnt>=ind:
        step=ind-csum-1
        j=jstart+step
        k=kstart-step
        print(i+1,j+1,k+1)
        exit()
    csum+=cnt