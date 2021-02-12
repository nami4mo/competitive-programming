n = int(input())
xyl = [tuple(map(int, input().split())) for _ in range(n)]

xyp = []
xym = []

for x,y in xyl:
    xyp.append(x+y)
    xym.append(x-y)

# xyp.sort()
# xym.sort()

ans1 = max(xym)-min(xym)
# print(ans1)
ans2 = max(xyp)-min(xyp)
ans = max(ans1,ans2)
print(ans)
