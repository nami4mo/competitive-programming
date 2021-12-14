

def main():
    n=int(input())
    al=list(map(int, input().split()))
    bl=list(map(int, input().split()))
    INF=10**18
    dp_same=[INF]*(n)
    dp_diff=[INF]*(n)
    
    dp_diff[0]=0
    # dp_same[0]=al[0]
    for i in range(n-1):
        dp_diff[i+1]=min(dp_diff[i+1], dp_diff[i]+bl[i], dp_same[i])
        dp_same[i+1]=min(dp_same[i+1], dp_same[i]+al[i+1]+bl[i], dp_diff[i]+al[i+1])
    
    # print(dp_diff)
    # print(dp_same)
    
    ans=min(dp_diff[n-1]+bl[n-1], dp_same[n-1])

    # print(ans)

    INF=10**18
    dp_same=[INF]*(n+1)
    dp_diff=[INF]*(n+1)
    
    # dp_diff[0]=0
    dp_same[0]=al[0]
    for i in range(n-1):
        dp_diff[i+1]=min(dp_diff[i+1], dp_diff[i]+bl[i], dp_same[i])
        dp_same[i+1]=min(dp_same[i+1], dp_same[i]+al[i+1]+bl[i], dp_diff[i]+al[i+1])

    ans2=min(dp_diff[n-1], dp_same[n-1]+bl[n-1])
    # print(ans,ans2)

    print(min(ans,ans2))

if __name__ == "__main__":
    main()