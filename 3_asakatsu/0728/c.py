n,m = map(int, input().split())

boxl = [1]*(n+1)
redl = [False]*(n+1)
redl[1] = True

for _ in range(m):
    x,y = map(int, input().split())
    if redl[x]:
        redl[y] = True
    if boxl[x] == 1:
        redl[x] = False
    boxl[x] -= 1
    boxl[y] += 1

ans = 0
for r in redl:
    if r: ans += 1

print(ans)