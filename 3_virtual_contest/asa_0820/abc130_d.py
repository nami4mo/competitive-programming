# from collections import deque

# n,k = map(int, input().split())
# al = list(map(int, input().split()))

# curr_sum = 0
# q = deque([])
# for i, a in enumerate(al):
#     curr_sum += a
#     if q 

from bisect import bisect_left, bisect_right

n,k = map(int, input().split())
al = list(map(int, input().split()))
al_cum = [0]

cum = 0
for a in al:
    cum += a
    al_cum.append(cum)

ans = 0
for i,a_cum in enumerate(al_cum):
    target = a_cum - k
    if target >= 0:
        cnt = bisect_right(al_cum, target)
        ans += cnt

print(ans)