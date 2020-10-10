ansl = []
MOD = 10**9+7
for _ in range(int(input())):
    n,a,b = map(int, input().split())
    if a+b > n:
        ansl.append(0)
        continue

    d = n-a-b
    no_cross = (d+1)*(d+2)
    no_cross %= MOD


    ans1 = no_cross * (n-a+1) * (n-b+1)
    ans1 %= MOD

    cross = (n-a+1)*(n-b+1) - no_cross
    ans2 = no_cross*cross
    ans2 %= MOD

    # print('no_corss',no_cross)
    # print('corss',cross)
    # print()
    
    ans = (ans1+ans2)%MOD
    ansl.append(ans)

for a in ansl: print(a)