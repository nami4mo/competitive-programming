from collections import deque
n=int(input())
al=list(map(int, input().split()))
q=deque(al)

lefts=[0]
csum=0
for i in range(n//2):
    white=q.popleft()
    black=q.popleft()
    flip=white*2+black+1
    csum+=flip
    lefts.append(csum)
    new_white=q.popleft()+white+black+2
    q.appendleft(new_white)

q=deque(al)
rights=[0]
csum=0
for i in range(n//2):
    white=q.pop()
    black=q.pop()
    flip=white*2+black+1
    csum+=flip
    rights.append(csum)
    new_white=q.pop()+white+black+2
    q.append(new_white)
    # print(q)

# print(lefts)
# print(rights)
ans=10**20
for i in range(n//2+1):
    v=lefts[i]+rights[n//2-i]
    ans=min(ans,v)
print(ans)