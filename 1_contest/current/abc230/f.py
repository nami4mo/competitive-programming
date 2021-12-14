

def main():
    n=int(input())
    al=list(map(int, input().split()))
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    zero=0
    zero_sum=0
    MOD=998244353
    for i in range(1,n):
        if al[i]==0:
            zero+=1
            dp[i+1]=dp[i]
            zero_sum+=1
        else:
            dp[i+1]+=(2+zero)*dp[i-zero]
            # dp[i+1]+=zero
            dp[i+1]%=MOD
            zero=0
    # print(dp)
    print(dp[n]%MOD)



if __name__ == "__main__":
    main()