import math

n = int(input())
al = list(map(int, input().split()))

cnt = 0
val = 0
for a in al:
    if a > 0:
        cnt += 1
        val += a

ans = math.ceil(val/cnt)
print(ans)