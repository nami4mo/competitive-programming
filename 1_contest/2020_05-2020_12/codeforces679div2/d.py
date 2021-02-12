from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
ql = []
for _ in range(2*n):
    ql.append(input().rstrip())

hq = []
ansl = []
for q in ql[::-1]:
    if q == '+':
        if not hq:
            print('NO')
            exit()
        else:
            v = heappop(hq)
            ansl.append(v)
    else:
        v = int(q.split()[1])
        if hq and v > hq[0]:
            print('NO')
            exit()
        else:
            heappush(hq,v)

print('YES')
print(*ansl[::-1])
