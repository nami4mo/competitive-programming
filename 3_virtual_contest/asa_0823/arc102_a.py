n,k = map(int, input().split())

if k%2 == 1:
    kcnt = n//k
    ans = pow(kcnt,3)
    print(ans)

else:
    kcnt = n//k
    ans = pow(kcnt,3)

    kcnt2 = 0
    for i in range(1,n+1):
        if i%k == (k//2): kcnt2 += 1
    ans += pow(kcnt2,3)
    print(ans)