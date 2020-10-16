from collections import deque

s = input()
q = deque()
ans = 0
for si in s:
    if q and q[-1] != si:
        q.pop()
        ans += 2
    else:
        q.append(si)
print(ans)