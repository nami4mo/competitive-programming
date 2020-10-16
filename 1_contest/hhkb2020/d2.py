MOD = 10**9+7
for _ in range(int(input())):
    n,a,b = map(int, input().split())
    if a+b > n:
        print(0)
        continue

    d = n-a-b
    no_overlap = (d+1)*(d+2)
    a_free = n-a+1
    b_free = n-b+1

    ans = no_overlap*a_free*b_free + (a_free*b_free-no_overlap)*no_overlap
    print(ans%MOD)