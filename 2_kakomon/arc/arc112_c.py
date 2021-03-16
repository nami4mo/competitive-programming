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
pl=list(map(int, input().split()))
gl=[[] for _ in range(n)]
for i,p in enumerate(pl):
    node=i+1
    pare=p-1
    gl[node].append(pare)
    gl[pare].append(node)
order,pare=make_order_parents(n,gl)

# 定義、そのマス（コインあり）にいるときに、どれだけ得するか
dp_val=[1]*n
dp_cnt=[1]*n

dp_toku=[[] for _ in range(n)]
dp_son=[[] for _ in range(n)]
dp_kougo=[[] for _ in range(n)]

for v in order[::-1]:
    #-- 子から送られてきた（ためていた）情報を処理
    dp_kougo[v].sort()
    for i in range(len(dp_kougo[v])):
        if i%2==0: dp_val[v]+=dp_kougo[v][i]
        else: dp_val[v]-=dp_kougo[v][i]

    for val in dp_son[v]: dp_val[v]-=val
    
    if len(dp_kougo[v])%2==0: dp_val[v]+=sum(dp_toku[v])
    else: dp_val[v]-=sum(dp_toku[v])

    if pare[v]==-1:continue

    #-- 親に情報を渡す
    dp_cnt[pare[v]]+=dp_cnt[v]
    if dp_cnt[v]%2==0:
        if dp_val[v]>0: dp_toku[pare[v]].append(dp_val[v])
        else: dp_son[pare[v]].append(dp_val[v]*(-1))
    else:
        dp_kougo[pare[v]].append(dp_val[v])

ans=(dp_val[0]+n)//2
print(ans)
