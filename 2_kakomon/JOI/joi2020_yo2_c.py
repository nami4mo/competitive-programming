n=int(input())
dp=[1]*(n+1)
for i in range(1,n+1):
    ksum=0
    for si in str(i):ksum+=int(si)
    if i+ksum<=n: dp[i+ksum]+=dp[i]

# print(dp)
print(dp[n])