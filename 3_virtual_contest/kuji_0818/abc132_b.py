n = int(input())
pl = list(map(int, input().split()))
ans = 0
for p1,p2,p3 in zip(pl[:-2],pl[1:-1],pl[2:]):
    if p1 < p2 and p2 < p3 or p1 > p2 and p2 > p3:
        ans += 1

print(ans)