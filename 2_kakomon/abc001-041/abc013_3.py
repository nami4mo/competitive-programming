from math import ceil
n,h = map(int, input().split())
a,b,c,d,e = map(int, input().split())

ans = 10**18
for i in range(n+1):
    need = e*i - h+1
    rem = n-i
    manzoku = d*rem
    cost = c*rem
    need -= manzoku
    add_a = ceil(need/(b-d))
    if add_a > rem:
        continue
    if add_a > 0:
        cost += add_a*(a-c)
    ans = min(ans,cost)

print(ans) 