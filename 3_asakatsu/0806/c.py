n = int(input())
al = list(map(int, input().split()))

accum = []
csum = 0
for a in al:
    csum += a
    accum.append(csum)

asum = accum[-1]
ans = 10**10
for a in accum[:-1]:
    x = a
    y = asum-x
    ans = min(ans, abs(x-y))

print(ans) 