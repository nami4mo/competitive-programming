n,m,c = map(int, input().split())
bl = list(map(int, input().split()))

ans = 0
for _ in range(n):
    al = list(map(int, input().split()))
    v = 0
    for a,b in zip(al,bl):
        v += a*b
    v+=c
    if v > 0: ans += 1

print(ans)