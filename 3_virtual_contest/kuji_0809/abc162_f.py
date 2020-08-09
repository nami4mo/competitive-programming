n = int(input())
al = list(map(int, input().split()))

if n%2 == 1:
    dp = [ [0]*4 for _ in range(n//2+1) ] 

    for i in range(n//2):
        dp[i+1][0] = dp[i][0] + al[i*2]
        dp[i+1][1] = max(dp[i][1]+al[i*2+1], dp[i][0]+al[i*2+1])
        dp[i+1][2] = max(dp[i][2]+al[i*2+2], dp[i][0]+al[i*2+2])
        dp[i+1][3] = max(dp[i][3]+al[i*2+2], dp[i][1]+al[i*2+2])
    ans = max(dp[-1])
    print(ans)

else:
    dp = [ [0]*2 for _ in range(n//2+1) ] 
    for i in range(n//2):
        dp[i+1][0] = dp[i][0] + al[i*2]
        dp[i+1][1] = max(dp[i][1]+al[i*2+1], dp[i][0]+al[i*2+1])
    ans = max(dp[-1])
    print(ans)