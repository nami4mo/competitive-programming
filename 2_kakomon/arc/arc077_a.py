from collections import deque
n=int(input())
al=list(map(int, input().split()))

q=deque()
if n%2==1:
    for i,a in enumerate(al):
        if i%2==0:
            q.appendleft(a)
        else:
            q.append(a)

else:
    for i,a in enumerate(al):
        if i%2==1:
            q.appendleft(a)
        else:
            q.append(a)

print(*list(q))