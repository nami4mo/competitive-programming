n,t=map(int, input().split())
tl=list(map(int, input().split()))
ans=0
for i in range(n-1):
    d=tl[i+1]-tl[i]
    d=min(d,t)
    ans+=d

ans+=t
print(ans)