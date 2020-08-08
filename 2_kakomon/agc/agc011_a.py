from collections import deque

n,c,k = map(int, input().split())
tl = []
for _ in range(n):
    t = int(input())
    tl.append(t)


tl.sort()
q = deque(tl)

ans = 0
while q:
    ans += 1
    poped = q.popleft()
    lim = poped + k
    for i in range(c-1):
        if not q:
            break
        next_t = q[0]
        if next_t <= lim:
            q.popleft()
        else:
            break

print(ans)