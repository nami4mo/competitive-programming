n = int(input())
al = list(map(int, input().split()))
ans = 10**18
for x in range(-100,101):
    v = 0
    for a in al:
        v += (a-x)**2
    ans = min(ans,v)

print(ans)