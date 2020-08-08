from collections import deque

h,w = map(int, input().split())
n = int(input())
al = list(map(int, input().split()))
ans = [ [0]*w for _ in range(h) ]

q = deque([])
for i,a in enumerate(al):
    c = i+1
    for _ in range(a):
        q.append(c)


for hi in range(h):
    for wi in range(w):
        if hi%2 == 0: ind = wi
        else: ind = ind = w-1-wi
        ans[hi][ind] = q.popleft()

for row in ans:
    print(*row)