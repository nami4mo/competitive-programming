n,k=map(int, input().split())
al=list(map(int, input().split()))
d={al[0]:1}
c=1
l,r=0,1
ans=0
while True:
    r+=1
    d.setdefault(al[r-1],0)
    d[al[r-1]]+=1
    if d[al[r-1]]==1:
        c+=1
    while c>k:
        d[al[l]]-=1
        if d[al[l]]==0:c-=1
        l+=1
    ans=max(ans,r-l)
    if r==n:break
print(ans)