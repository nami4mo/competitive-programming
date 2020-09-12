import heapq
from bisect import bisect_left, bisect_right

n = int(input())
a = int(input())
q = [a*(-1)]
# ans = 1

for _ in range(n-1):
    a = int(input())
    # bより大きい最小要素のindex/value
    ind = bisect_right(q, a*(-1))
    ind = ind if 0 <= ind < len(q) else None
    if ind is None:
        q.append(a*(-1))
    else:
        q[ind] = a*(-1)

print(len(q))