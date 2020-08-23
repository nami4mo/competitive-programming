n,m = map(int, input().split())
redl = [False]*(n+1)
redl[1] = True
cnts = [1]*(n+1)
cnts[0] = 1

for _ in range(m):
    x,y = map(int, input().split())
    if redl[x]: redl[y] = True
    if cnts[x] == 1: redl[x] = False
    cnts[x] -= 1
    cnts[y] += 1

ans = redl.count(True)
print(ans)