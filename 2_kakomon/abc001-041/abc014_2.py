n,x=map(int, input().split())
al=list(map(int, input().split()))
ans=0
for i in range(n):
    if x&(1<<i):ans+=al[i]
print(ans)