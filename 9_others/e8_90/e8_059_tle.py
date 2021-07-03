import sys
input = sys.stdin.readline

n,m,q=map(int, input().split())
gl=[[] for _ in range(n)]
for _ in range(m):
    x,y=map(int, input().split())
    x-=1
    y-=1
    gl[x].append(y)

def solve(ql):
    dp=[0]*n
    qn=len(ql)
    for i in range(qn):
        l,_ = ql[i]
        dp[l]|=(1<<i)
    for i in range(n):
        v=dp[i]
        for neib in gl[i]:
            dp[neib] |= dp[i]
    for i in range(qn):
        _,r = ql[i]
        if dp[r] & (1<<i):
            print('Yes')
        else:
            print('No')

ql=[]
for i in range(q):
    a,b=map(int, input().split())
    a-=1
    b-=1
    ql.append((a,b))  
    if i%64==63 or i==q-1:
        solve(ql)
        ql=[]
