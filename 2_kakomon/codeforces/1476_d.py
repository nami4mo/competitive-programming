import sys
input = sys.stdin.readline

ansl=[]
for _ in range(int(input())):
    n=int(input())
    s=input()
    dp=[0]*(n+1)
    dpr=[0]*(n+1)
    for i in range(n,0,-1):
        if s[i-1]=='R':
            dp[i-1]=dpr[i]+1
        else:
            dpr[i-1]=dp[i]+1
    rights=[0]*(n+1)
    for i in range(n): 
        if s[i]=='R':rights[i]=dp[i]

    dp=[0]*(n+1)
    dpr=[0]*(n+1)
    for i in range(0,n):
        if s[i]=='L':
            dp[i+1]=dpr[i]+1
        else:
            dpr[i+1]=dp[i]+1
    lefts=[0]*(n+1)
    for i in range(1,n+1): 
        if s[i-1]=='L':lefts[i]=dp[i]
    # print(lefts)
    ans=[]
    for i in range(n+1):ans.append(lefts[i]+rights[i]+1)
    ansl.append(ans)

for row in ansl:print(*row)