n,m = map(int, input().split())
ls = []
rs = []
for _ in range(m):
    l,r = map(int, input().split())
    ls.append(l)
    rs.append(r)

ls.sort()
rs.sort()

ans = rs[0] - ls[-1] + 1
ans = max(0,ans)

print(ans)