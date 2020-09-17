from heapq import heapify, heappop, heappush
from collections import deque

n,k = map(int, input().split())
dtl = []
# t_dmax = [-1]*(n+1)
for _ in range(n):
    t,d = map(int, input().split())
    dtl.append((d,t))


dtl.sort(reverse=True)
dtq = deque(dtl)

dt_remq = deque([])
already_t = [False]*(n+1)
tll = [ [] for _ in range(n+1)]
cnt = 0
oisi = 0
kl = []
while dtq:
    d,t = dtq.popleft()
    if k <= cnt or already_t[t]: 
        dt_remq.append((d,t))
    else:
        already_t[t] = True
        kl.append((d,t))
        tll[t].append(d)
        cnt += 1
        oisi += d


rem = k-cnt
# if rem == 0:
#     ans = oisi + k*k
#     print(ans)
#     exit()

more_twos = []
for _ in range(rem):
    d,t = dt_remq.popleft()
    tll[t].append(d)
    oisi += d

ones = []
for tl in tll:
    if len(tl) == 1: ones.append(tl[0])

ones.sort()
onesq = deque(ones)

cuur_v = oisi + cnt*cnt
# print(cuur_v)
# print(kl,cnt)
while dt_remq and onesq:
    d,t = dt_remq.popleft()
    oisi_diff = d-onesq[0]
    bonus_diff = cnt*cnt-(cnt-1)*(cnt-1)
    if oisi_diff > bonus_diff:
        cuur_v += (oisi_diff-bonus_diff)
        cnt -= 1
        onesq.popleft()
    else:
        break

print(cuur_v)