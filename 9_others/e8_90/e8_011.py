n=int(input())
dcsl=[]
for _ in range(n):
    d,c,s=map(int, input().split())
    start=d-c
    dcsl.append((d,c,s))

dcsl.sort(key=lambda x:x[0])
MAX=5000+5000
dp=[0]*(MAX+1)
for i in range(n):
    new_dp=[0]*(MAX+1)
    d,c,s=dcsl[i]
    for j in range(1,MAX):
        new_dp[j]=max(new_dp[j], dp[j])
        if j+(c-1)>d:
            pass
        else:
            new_dp[j+c]=max(new_dp[j+c], dp[j+c], dp[j]+s)
    dp=new_dp[:]

ans=max(dp)
print(ans)