from collections import deque
n=int(input())
s=list(input())
q=deque()

def do(q,c):
    if abs(c)>len(q):return 'ERROR'
    if c>0:
        tmps=deque()
        for i in range(c):
            tmps.append(q.popleft())
        res=(tmps.pop())
        for i in range(c-1):
            q.appendleft(tmps.pop())
        return res
    else:
        tmps=deque()
        c=abs(c)
        for i in range(c):
            tmps.appendleft(q.pop())
        res=tmps.popleft()
        for i in range(c-1):
            q.append(tmps.popleft())
        return res

qs={'A':1,'B':2,'C':3,'D':-1,'E':-2,'F':-3}
for i,si in enumerate(s):
    if si=='L':q.appendleft(i+1)
    elif si=='R':q.append(i+1)
    else:print(do(q,qs[si]))
    # print(q)