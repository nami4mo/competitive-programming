n = int(input())
bl = list(map(int, input().split()))
bl = [10**6] + bl + [10**6]

ans = 0
for b1,b2 in zip(bl[:-1],bl[1:]):
    ans += min(b1,b2)

print(ans)