

def main():
    n=int(input())
    al=list(map(int, input().split()))
    bl=list(map(int, input().split()))
    MAX=3001
    dp=[[0]*(MAX) for _ in range(n+1)]
    dp[0][0]=1
    MOD=998244353
    for i in range(n):
        a,b=al[i],bl[i]
        csum=0
        for j in range(MAX):
            if j>b:break
            csum+=dp[i][j]
            csum%=MOD
            if a<=j:
                dp[i+1][j]+=csum
                dp[i+1][j]%=MOD
    ans=sum(dp[n])%MOD
    print(ans)


if __name__ == "__main__":
    main()