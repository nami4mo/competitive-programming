n=int(input())
hl=[int(input()) for _ in range(n)]
ls=[0]*n
rs=[0]*n

v=0
for i in range(1,n):
    if hl[i-1]<hl[i]: v+=1
    else:v=0
    ls[i]=v

v=0
for i in range(n-2,-1,-1):
    if hl[i]>hl[i+1]: v+=1
    else:v=0
    rs[i]=v

ans=0
for i in range(n):
    v=ls[i]+rs[i]+1
    ans=max(ans,v)
print(ans)