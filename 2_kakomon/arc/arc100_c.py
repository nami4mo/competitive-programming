n=int(input())
al=list(map(int, input().split()))
dp=[(a,-1) for a in al]

for j in range(n):
    bit=1<<j
    for i in range(2**n):
        if i&bit:
            # dp[i] += dp[i^bit]
            a,b=dp[i]
            c,d=dp[i^bit]
            vs=[a,b,c,d]
            vs.sort(reverse=True)
            dp[i]=(vs[0],vs[1])
cmax=0
for a,b in dp[1:]:
    v=a+b
    cmax=max(cmax,v)
    print(cmax)