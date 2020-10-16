MOD = 10**9+7
for _ in range(int(input())):
    n,a,b = map(int, input().split())
    d = n-a-b
    if d < 0: 
        print(0)
        continue
    no_cross = (d+1)*(d+2)
    cross = (n-a+1)*(n-b+1)-no_cross
    ans = (n-a+1)*(n-b+1)*(n-a+1)*(n-b+1) - cross*cross
    print(ans%MOD)