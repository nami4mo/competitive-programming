from collections import deque

h,w = map(int, input().split())
n = int(input())
al = list(map(int, input().split()))

q = deque([])
for i,a in enumerate(al):
    c = i+1
    for j in range(a):
        q.append(c)

ans = [ [0]*w for _ in range(h)]
for hi in range(h):
    if hi%2 == 0:
        for wi in range(w):
            c = q.popleft()
            ans[hi][wi] = c
    else:
        for wi in range(w-1,-1,-1):
            c = q.popleft()
            ans[hi][wi] = c

    
for a in ans:
    print(*a)