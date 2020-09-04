from collections import deque

s = list(input())
Q = int(input())
r = False

q = deque(s)
for _ in range(Q):
    query = list(map(str, input().split()))
    if query[0] == '1':
        r = not r
    else:
        f,c = query[1],query[2]
        if f == '1':
            if not r:
                q.appendleft(c)
            else:
                q.append(c)
        else:
            if not r:
                q.append(c)
            else:
                q.appendleft(c)

ans = list(q)
if r: ans = ans[::-1]
print(''.join(ans))
