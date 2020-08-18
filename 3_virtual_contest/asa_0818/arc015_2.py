n = int(input())
ans = [0]*6
for _ in range(n):
    ma, mi = map(float, input().split())
    if ma >= 35.0:
        ans[0] += 1
    elif ma >= 30.0:
        ans[1] += 1
    elif  ma >= 25.0:
        ans[2] += 1
    if mi >= 25.0:
        ans[3] += 1
    if ma >= 0.0 and mi < 0.0:
        ans[4] += 1
    if ma < 0.0:
        ans[5] += 1

print(*ans)