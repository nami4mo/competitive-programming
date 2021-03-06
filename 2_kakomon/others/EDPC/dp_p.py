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
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

order,pare=make_order_parents(n,gl)
# print(order[::-1],pare)

'''
    親側に情報だけ渡す → 親は自分の番がきたときに、集まった情報を処理して値を出す
'''
# dp_b=[0]*n
# dp_w=[0]*n
# pool_bw=[[] for _ in range(n)]
# pool_w=[[] for _ in range(n)]
# MOD=10**9+7
# for v in order[::-1]:
#     black,white=1,1
#     for cw in pool_w[v]: black*=cw
#     for cbw in pool_bw[v]: white*=cbw
#     dp_b[v]=black%MOD
#     dp_w[v]=white%MOD
#     if pare[v]==-1:continue
#     pool_bw[pare[v]].append(dp_b[v]+dp_w[v])
#     pool_w[pare[v]].append(dp_w[v])

'''
    親の値を子どもが更新する
'''
dp_b=[1]*n
dp_w=[1]*n
MOD=10**9+7
for v in order[::-1]:
    if pare[v]==-1:continue
    dp_b[pare[v]]*=dp_w[v]
    dp_w[pare[v]]*=(dp_w[v]+dp_b[v])
    dp_b[pare[v]]%=MOD
    dp_w[pare[v]]%=MOD

print((dp_w[0]+dp_b[0])%MOD)