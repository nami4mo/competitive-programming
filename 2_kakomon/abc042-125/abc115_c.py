n,k = map(int, input().split())
hl = []
for _ in range(n):
    hl.append(int(input()))

hl.sort()
ans = 10**18
for i in range(n-k+1):
    hmin = hl[i]
    hmax = hl[i+k-1]
    ans = min(ans, hmax-hmin)

print(ans)
