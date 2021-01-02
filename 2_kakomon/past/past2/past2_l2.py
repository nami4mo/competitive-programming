from heapq import heapify, heappop, heappush

n,k,d = map(int, input().split())
al = list(map(int, input().split()))

q = []

if d*(k-1)+1 > n:
    print(-1)
    exit()

pushed_i = 0
l = 0
ansl = []
for i in range(k):
    rem = k-i
    r = n-(rem-1)*d
    for j in range(pushed_i,r):
        heappush(q,(al[j],j))
    pushed_i = r-1
  
    while q[0][1] < l:
        heappop(q)

    selected_i = 0
    amin = q[0][0]
    for j in range(l,r):
        if al[j] == amin:
            selected_i = j
            break
    l = selected_i + d
    ansl.append(amin)

print(*ansl)
