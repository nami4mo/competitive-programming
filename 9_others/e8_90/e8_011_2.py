n=int(input())
dcsl=[]
for _ in range(n):
    d,c,s=map(int, input().split())
    start=d-c
    dcsl.append((d,c,s))

dcsl.sort(key=lambda x:x[0], reverse=True)
MAX=5000+5000
dp=[0]*(MAX+1)
for i in range(n):
    new_dp=[0]*(MAX+1)
    cmax=0
    d,c,s=dcsl[i]
    for j in range(MAX,0,-1):
        if j+(c-1)>d:
            # v=dp[j+c]
            v=dp[j]
            cmax=max(cmax,v)
        else:
            v=max(dp[j],dp[j+c]+s)
            cmax=max(cmax,v)
        new_dp[j]=cmax
    dp=new_dp[:]

ans=max(dp)
print(ans)