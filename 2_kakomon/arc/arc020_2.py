n,c=map(int, input().split())
al=[int(input()) for _ in range(n)]
ans=10**18
for i in range(1,11):
    for j in range(1,11):
        if i==j:continue
        v=0
        for k in range(n):
            if k%2==0 and al[k]!=i:v+=c
            if k%2==1 and al[k]!=j:v+=c
        ans=min(ans,v)
print(ans)