from collections import deque

def fail():
    print(-1)
    exit()

n=int(input())
s=input()
t=input()

sq = deque()
tq = deque()
for i in range(n):
    if s[i]=='1': sq.append(i)
    if t[i]=='1': tq.append(i)

ans = 0
while sq:
    if not tq:
        if len(sq)%2 == 1: fail()
        for i in range(len(sq)//2):
            ans += (sq[1]-sq[0])
            sq.popleft()
            sq.popleft()
        print(ans)
        exit()

    if sq[0] > tq[0]:
        ans += (sq[0]-tq[0])
        sq.popleft()
        tq.popleft()

    elif sq[0] == tq[0]:
        sq.popleft()
        tq.popleft()

    elif sq[0] < tq[0]:
        if len(sq)==1:fail()
        cost = sq[1] - sq[0]
        ans += cost
        sq.popleft()
        sq.popleft()


    # print(ans)
    # print(sq)
if tq:fail()
print(ans)