n,m = map(int, input().split())
abl = []
for _ in range(n):
    a,b = map(int, input().split())
    abl.append((a,b))

abl.sort()

ans = 0
cnt = 0
for a,b in abl:
    rem = m-cnt
    if rem > b:
        cnt += b
        ans += a*b
    else:
        ans += rem*a
        break

print(ans)