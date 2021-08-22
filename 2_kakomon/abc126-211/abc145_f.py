from copy import copy

n,k=map(int, input().split())
hl=list(map(int, input().split()))
dp=[{} for i in range(k+1)] # inline

dp[0] = {0:0}
for i in range(n):
    new_dp=[{} for i in range(k+1)]
    h=hl[i]
    for j in range(k+1):
        for key,v in dp[j].items():
            # not erase
            if key <= h:
                if h in new_dp[j]:
                    new_dp[j][h] = min(v+(h-key), new_dp[j][h])
                else:
                    new_dp[j][h] = v+(h-key)
            else:
                if h in new_dp[j]:
                    new_dp[j][h] = min(v, new_dp[j][h])
                else:
                    new_dp[j][h] = v
            # erase
            if j+1<=k:
                if key in new_dp[j+1]:
                    new_dp[j+1][key] = min(v, new_dp[j+1][key])  
                else:
                    new_dp[j+1][key] = v 
    # print(i)
    # print(new_dp)
    dp=copy(new_dp)     
    
# ans = 10**18
ans=min(dp[-1].values())
print(ans)
# print(dp)