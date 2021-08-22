n,k=map(int, input().split())
lrs=[]
for _ in range(k):
    l,r=map(int, input().split())
    lrs.append((l,r))
lrs.sort()
# print(lrs)
MOD=998244353
dp=[0]*(n)
dp[0]=1
sdp=[0,1]
for i in range(1,n):
    # print('---',i)
    for j in range(k):
        l,r=lrs[j]
        li=max(0,i-r)
        ri=max(0,i-l+1)
        dp[i]+=(sdp[ri]-sdp[li])
        # print(li,ri)
        # print('v',sdp[li],sdp[ri])
    dp[i]%=MOD
    sdp.append((sdp[-1]+dp[i])%MOD)
print(dp[-1])