n,k=map(int, input().split())
al=list(map(int, input().split()))

csum=sum(al[:k])
ans=csum
for i in range(n-k):
    poped=al[i]
    inserted=al[k+i]
    csum-=poped
    csum+=inserted
    ans+=csum
print(ans)
