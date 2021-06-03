n,k=map(int, input().split())
ps=[0]*(n+1)
for i in range(2,n+1):
    if ps[i]>0:continue
    for j in range(i,n+1,i):
        ps[j]+=1

ans=0
for i in range(2,n+1):
    if ps[i]>=k:ans+=1
print(ans)