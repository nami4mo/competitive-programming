n,k = map(int, input().split())
k = abs(k)

ans = 0
for i in range(k+2,2*n+1):
    if i <= n:
        abc = i-1
        cdk = i-k
        # print('cdk',cdk)
        if cdk <= n:
            cdc = max(0,cdk-1)
        else:
            cdc = max(0, 2*n-cdk+1)
        ans += abc*cdc
    else:
        abc = max(0, 2*n-i+1)
        cdk = i-k
        # print('cdk',cdk)
        if cdk <= n:
            cdc = max(0,cdk-1)
        else:
            cdc = max(0, 2*n-cdk+1)
        ans += abc*cdc
    # print(abc,cdc)
print(ans)