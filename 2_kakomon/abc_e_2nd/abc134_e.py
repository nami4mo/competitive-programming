# from heapq import heappop, heappush
from bisect import bisect_left, bisect_right

n=int(input())
q=[]
for _ in range(n):
    v=int(input())*(-1)
    if not q: q.append(v)
    else:
        ind = bisect_right(q, v)
        if 0 <= ind < len(q):
            q[ind]=v
        else:
            q.append(v)
print(len(q))
