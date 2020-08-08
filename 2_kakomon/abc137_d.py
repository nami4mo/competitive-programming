import heapq

N, M = map(int, input().split()) 

day_rew = {}
for _ in range(N):
    a, b = map(int, input().split()) 
    day_rew.setdefault(a,[])
    day_rew[a].append(b)

ans = 0
job_rew = []
heapq.heapify(job_rew)
for i in range(1, M+1):
    if i in day_rew:
        for r in day_rew[i]:
            heapq.heappush(job_rew, r*(-1))
    if job_rew:
        this_day_rew = heapq.heappop(job_rew)*(-1)
        ans += this_day_rew

print(ans)

