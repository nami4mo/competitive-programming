gl=[
    [1],
    [0,2,4],
    [1,3,5],
    [2,6],
    [1,5,7],
    [2,4,6,8],
    [3,5,9],
    [4,8],
    [5,7,9],
    [6,8]
]

INF=10**10
m,r=map(int, input().split())
dp=[[INF]*m for _ in range(10)]
dp[0][0]=0

from collections import deque
q=deque()
q.append((0,0))
while True:
    # print(q)
    pos,rem=q.popleft()
    cost=dp[pos][rem]
    new_rem=(rem*10+pos)%m
    if dp[pos][new_rem]==INF:
        dp[pos][new_rem]=cost+1
        q.append((pos,new_rem))
    if new_rem==r:
        print(cost+1)
        break
    for neib in gl[pos]:
        if dp[neib][rem]==INF:
            dp[neib][rem]=cost+1
            q.append((neib,rem))