n = int(input())
al = list(map(int, input().split()))
asum = 0
for a in al:
    asum = asum^a


ans = []
for a in al:
    v = asum^a
    ans.append(v)

print(*ans)