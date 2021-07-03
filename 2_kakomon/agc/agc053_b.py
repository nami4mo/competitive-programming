from heapq import heapify, heappop, heappush, heappushpop
n=int(input())
vl=list(map(int, input().split()))

q=[]
ans=0
for i in range(n):
    heappush(q, vl[n-i-1])
    heappush(q, vl[n+i])
    v=heappop(q)
    ans+=v
print(sum(vl)-ans)