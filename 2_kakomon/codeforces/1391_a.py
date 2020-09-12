from collections import deque

for _ in range(int(input())):
    n = int(input())
    q = deque([])
    for i in range(1,n+1):
        if i%2 == 0:
            q.appendleft(i)
        else:
            q.append(i)
    print(*list(q))