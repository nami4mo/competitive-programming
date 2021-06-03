from collections import deque
def make_order_parents(n,gl,root=0):
    order=[root]
    parents=[-1]*n
    q=deque([root])
    while q:
        poped=q.popleft()
        for neib in gl[poped]:
            if parents[neib]!=-1 or neib==root:continue
            parents[neib]=poped
            order.append(neib)
            q.append(neib)
    return order,parents

n=int(input())
gl=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, input().split())
    gl[a-1].append(b-1)
    gl[b-1].append(a-1)
order,pare=make_order_parents(n,gl)

dp=[1]*n
ans=0
for v in order[::-1]:
    if pare[v]==-1:continue
    dp[pare[v]]+=dp[v]
    ans+=dp[v]*(n-dp[v])

print(ans)