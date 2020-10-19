from bisect import bisect_left, bisect_right

n,k = map(int, input().split())
al = list(map(int, input().split()))

# dp = [ [False]*(k+1) for _ in range(n+1) ]
dp = [ set() for _ in range(n+1) ]

dp[0].add(0)
for i in range(n):
    a = al[i]
    for v in dp[i]:
        dp[i+1].add(v)
        if v+a < k: dp[i+1].add(v+a)
        
# dp = dp[1:]
for i in range(n+1):
    dp[i] = list(dp[i])
    dp[i].sort()


dpr = [ set() for _ in range(n+1) ]
alr = al[::-1]

dpr[0].add(0)
for i in range(n):
    a = alr[i]
    for v in dpr[i]:
        dpr[i+1].add(v)
        if v+a < k: dpr[i+1].add(v+a)

# dpr = dpr[1:]
# dpr = dpr[::-1]

for i in range(n+1):
    dpr[i] = list(dpr[i])
    dpr[i].sort()

# print(dp)
# print(dpr)

ans = 0
for i in range(n):
    a = al[i]
    for lv in dp[i]:
        cnt1 = len(dpr[n-i-1]) - bisect_left(dpr[n-i-1], k-lv)
        cnt2 = len(dpr[n-i-1]) - bisect_left(dpr[n-i-1], k-lv-a)
        if cnt2 - cnt1 != 0: break
    else:
        ans+=1

print(ans)