# WA!

from collections import deque

n,d,m = map(int, input().split())
al = list(map(int, input().split()))

alm = []
alnom = []
for a in al:
    if a > m: alm.append(a)
    else: alnom.append(a)

alm.sort(reverse=True)
alnom.sort(reverse=True)
alm_q = deque(alm)
alnom_q = deque(alnom)

next_nom_sum = 0
for i in range(min((d+1),len(alnom))):
    next_nom_sum += alnom[i]

# print(alm)
# print(alnom)

if alm_q:
    rem = n-1
    ans = alm_q.popleft()
    while True:
        if alm_q and alm_q[0] >= next_nom_sum and rem >= d+1:
            poped = alm_q.popleft()
            # print(poped,'m')
            ans += poped
            for i in range(d):
                if alnom_q:
                    poped = alnom_q.pop()
                    if len(alm_q) < d+1:
                        next_nom_sum -= poped
                else:
                    alm_q.pop()
            rem -= (d+1)
        else:
            if alnom_q:
                poped = alnom_q.popleft()
                # print(poped,'nom')
                ans += poped
                next_nom_sum -= poped
                if len(alnom_q) >= d+1:
                    next_nom_sum += alnom_q[d]
                # print(next_nom_sum)
            else:
                alm_q.pop()
            rem -= 1

        if rem <= 0:
            break
else:
    ans = sum(alnom)

print(ans)