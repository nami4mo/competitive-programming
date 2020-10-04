from itertools import combinations

n,m,p,q,r = map(int, input().split())
girl_yzl = [ [0]*(m) for _ in range(n) ]
for _ in range(r):
    x,y,z = map(int, input().split())
    x-=1
    y-=1
    girl_yzl[x][y] = z

ll = list(range(0,n))  # list of elements
combl = list(combinations(ll, p))

ans = 0
for comb in combl:
    boys = [0]*m
    for girl in comb:
        curr_girl = girl_yzl[girl]
        for boy, happy in enumerate(curr_girl):
            boys[boy] += happy
    boys.sort(reverse=True)
    ans = max(ans, sum(boys[:q]))

print(ans)