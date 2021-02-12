# print('spam', flush=True)
# sys.stdout.flush()
import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
if n == 1:
    print('!',1)
ansl = [0]*(n+1)

q = deque(list(range(1,n+1)))

for _ in range(n):
    l = q.popleft()
    if not q:
        ansl[l] = n
        break
    r = q.popleft()
    print('?',l,r,flush=True)
    a = int(input())
    print('?',r,l,flush=True)
    b = int(input())

    if a < b:
        ansl[r] = b
        q.append(l)
    else:
        ansl[l] = a
        q.append(r)


print('!',*ansl[1:])
