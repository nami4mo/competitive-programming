n,d = map(int, input().split())
d2 = d**2
ans = 0
for _ in range(n):
    x,y = map(int, input().split())
    xy = x**2 + y**2
    if xy <= d2:
        ans += 1

print(ans)