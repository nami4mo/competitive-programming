n,a,b = map(int, input().split())
xl = list(map(int, input().split()))


ans = 0
for x1,x2 in zip(xl[:-1],xl[1:]):
    diff = x2-x1
    walk_cost = diff*a
    ans += min(walk_cost, b)

print(ans)