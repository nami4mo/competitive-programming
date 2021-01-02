from collections import deque
al=list(input())
bl=list(input())
cl=list(input())
aq=deque(al)
bq=deque(bl)
cq=deque(cl)
next_t='a'
while True:
    if next_t=='a':
        if not aq:
            print('A')
            exit()
        else:
            next_t=aq.popleft()
    elif next_t=='b':
        if not bq:
            print('B')
            exit()
        else:
            next_t=bq.popleft()
    elif next_t=='c':
        if not cq:
            print('C')
            exit()
        else:
            next_t=cq.popleft()