n = int(input())
pl = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    if pl[i] == i+1:
        ans += 1
        pl[i], pl[i+1] = pl[i+1], pl[i]
    
if pl[n-1] == n: ans += 1
print(ans)