import heapq

n = int(input())
abl = [ [] for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split()) 
    abl[a].append(b)

curr_p = 0
tasks = []
heapq.heapify(tasks)
for i in range(n):
    day = i+1
    for v in abl[day]:
        heapq.heappush(tasks, -1*v)
    p = heapq.heappop(tasks)*(-1)
    curr_p += p
    print(curr_p)
