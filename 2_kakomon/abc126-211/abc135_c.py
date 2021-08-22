n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

ans = 0
killed = 0
for i in range(n):
    rem_a = al[i] - killed
    if bl[i] >= rem_a:
        ans += rem_a
        rem_b = bl[i] - rem_a
        if rem_b >= al[i+1]:
            ans += al[i+1]
            killed = al[i+1]
        else:
            ans += rem_b
            killed = rem_b
    else:
        ans += bl[i]
        killed = 0
print(ans)