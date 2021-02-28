import sys
sys.setrecursionlimit(10**7)
MOD=998244353
dp=[[-1]*3001 for _ in range(3001)]
def rec(i,j):
    if i==j:return 1
    if i<j:return 0
    if j<=0 or i<=0: return 0
    if dp[i][j]!=-1:return dp[i][j]
    dp[i][j]=rec(i-1,j-1)+rec(i,2*j)
    dp[i][j]%=MOD
    return dp[i][j]

n,k=map(int, input().split())
ans=rec(n,k)
print(ans)