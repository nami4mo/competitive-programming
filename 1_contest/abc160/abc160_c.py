
k,n = map(int, input().split())
al = list(map(int, input().split()))
al.sort()

ans = 10**18
for start_i in range(n):

    if start_i == 0:
        clock = al[-1] - al[0]
    else:
        clock = k - al[start_i] + al[start_i-1]

    if start_i == n-1:
        c_clock = al[-1] - al[0]
    else:
        goal = start_i+1
        c_clock = al[start_i] + (k-al[goal]) 

    ans = min(ans, clock, c_clock)
    # print(clock)
    # print(c_clock)

print(ans)