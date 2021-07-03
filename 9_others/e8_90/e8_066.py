def prob(l1,r1,l2,r2):
    if r1<=l2:
        return 0
    if r2<l1:
        return 1
    cnt=0
    for i1 in range(l1,r1+1):
        for i2 in range(l2,r2+1):
            if i1>i2:cnt+=1
    return cnt/((r1-l1+1)*(r2-l2+1))
    

n=int(input())
al=[]
for _ in range(n):
    l,r=map(int, input().split())
    al.append((l,r))

ans=0
for i1 in range(n-1):
    l1,r1=al[i1]
    for i2 in range(i1+1,n):
        l2,r2=al[i2]
        p=prob(l1,r1,l2,r2)
        ans+=p
print(ans)