from heapq import heappop, heappush, heapify
n,m = map(int, input().split())
al = list(map(int, input().split()))
alm = []
for a in al:
    alm.append(a*(-1))

heapify(alm)
for _ in range(m):
    poped = heappop(alm)
    val = (poped*(-1))//2
    heappush(alm, val*(-1))

ans = sum(alm)
print(-ans)
