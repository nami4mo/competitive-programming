n,t=map(int, input().split())
al=list(map(int, input().split()))
ans=0
for i in range(n-1):
    d=al[i+1]-al[i]
    d=min(d,t)
    ans+=d
ans+=t
print(ans)