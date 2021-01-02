from collections import deque
s=input()
q=deque()
for si in s:
    if si=='B':
        if q: q.pop()
    else:
        q.append(si)
print(''.join(list(q)))