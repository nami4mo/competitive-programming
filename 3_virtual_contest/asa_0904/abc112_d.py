n,m = map(int, input().split())

ans = 1
for i in range(1,10**5):
    if m%i == 0:
        v = i
        cnt = m//i
        if cnt >= n:
            ans = max(ans,v)

        v = m//i
        cnt = i
        if cnt >= n:
            ans = max(ans,v)

print(ans)