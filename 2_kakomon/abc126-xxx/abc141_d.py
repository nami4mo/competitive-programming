import heapq
n,m = map(int, input().split())
al = list(map(int, input().split()))
al = [(-1)*a for a in al]
al.sort()

for _ in range(m):
    poped = heapq.heappop(al)
    heapq.heappush(al, (poped*(-1)//2)*(-1))

print(sum(al)*(-1))