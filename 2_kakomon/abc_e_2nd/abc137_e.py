'''
    [bellman_ford]
    # g...  list of edges [ (from,to,cost), (from,to,cost), ...]
    # 負の閉路がゴールにたどりつくか判定するには、n-1回のループの後、距離更新時にINFを伝搬させるループをさらにn-1回行う (abc061_d)
    # もしくは、ゴールから逆順に辿った頂点 と スタートから辿った頂点 の＆をとって、不要な頂点（ゴールにたどり着かない閉路）を消す
'''
def bellman_ford(s, n, g): # s: start, n: |V|, g; glaph 
    INF = 10**18
    d = [INF]*n
    d[s] = 0
    for i in range(n): # max n-1 loops. if update d[] in n-th loop -> negative cycle
        update = False
        for v_from, v_to, cost in g:
            if d[v_from] != INF and d[v_to] > d[v_from] + cost:
                d[v_to] = d[v_from] + cost
                update = True
        if not update:
            return d
    else: # if not break until n-th loop -> detect negative cycle
        # may do something for negatice cycle
        return None


n,m,p=map(int, input().split())
gl=[]
gll=[[] for _ in range(n)]
for _ in range(m):
    u,v,c=map(int, input().split())
    u-=1
    v-=1
    c-=p
    gl.append((u,v,-c))
    gll[v].append(u)

from collections import deque
q=deque([n-1])
visited=[False]*n
visited[n-1]=True
while q:
    poped=q.popleft()
    for neib in gll[poped]:
        if visited[neib]:continue
        q.append(neib)
        visited[neib]=True


new_gl=[]
for u,v,c in gl:
    if not visited[v] or not visited[u]:continue
    new_gl.append((u,v,c))

d=bellman_ford(0,n,new_gl)
if d is None:
    print(-1)
else:
    ans=d[n-1]*(-1)
    ans=max(0,ans)
    print(ans)