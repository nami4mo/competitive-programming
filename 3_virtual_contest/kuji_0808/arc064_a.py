
n,x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(0,n-1):
    if a[i] + a[i+1] > x:
        rem = (a[i]+a[i+1]) - x
        if rem <= a[i+1]:
            ans += rem
            a[i+1] -= rem
        else:
            ans += rem
            a[i+1] = 0

print(ans)