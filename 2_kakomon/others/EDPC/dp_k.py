import sys
sys.setrecursionlimit(10**6)
def rec(dp, al, v):
    if v == 0:
        dp[v] = 1
        return -1
    if dp[v] != 0:
        return dp[v]
    ans = -1
    for a in al:
        if v-a < 0: continue
        if rec(dp, al, v-a) == -1:
            ans = 1
            break
    dp[v] = ans
    return ans

n,k = map(int, input().split())
al = list(map(int, input().split()))
dp = [0]*(k+1)
ans = rec(dp,al,k)

# print(dp)

if ans == 1:
    print('First')
else:
    print('Second')
