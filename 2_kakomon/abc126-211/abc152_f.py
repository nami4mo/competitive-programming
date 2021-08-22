def dfs(cst_num, goal, pare, node, gl, edges_num):
    val_flag = False
    for neib in gl[node]:
        if pare==neib: continue
        route_flag = dfs(cst_num, goal, node, neib, gl, edges_num)
        if route_flag:
            edges_num[min(node,neib),max(node,neib)] += cst_num
            val_flag = True
    if val_flag or node == goal:
        return True
    else:
        return False

n=int(input())
gl=[ [] for _ in range(n)]
edges_num = {}
for _ in range(n-1):
    a,b = map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)
    edges_num[(min(a,b),max(a,b))] = 0

m=int(input())
crs = []
for _ in range(m):
    u,v=map(int, input().split())
    u-=1
    v-=1
    crs.append((u,v))

for i in range(m):
    u,v = crs[i]
    cst_num = 2**i
    dfs(cst_num, v, -1, u, gl, edges_num)

notans = 0
# MOD = 10**9+7
for i in range(1,2**m):
    pop_cnt = bin(i).count('1')
    white_cnt = 0
    for v in edges_num.values():
        if v&i > 0:
            white_cnt+=1
    rem = n-1-white_cnt
    comb = pow(2,rem)
    if pop_cnt%2 == 1:
        notans+=comb
    else:
        notans-=comb

ans = pow(2,n-1)-notans
print(ans)