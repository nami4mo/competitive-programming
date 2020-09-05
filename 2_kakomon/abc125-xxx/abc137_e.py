INF = 10**18
def bellman_ford(s, n, g): # s: start, n: |V|, g; glaph 
    d = [INF]*n
    d[s] = 0
    for i in range(n-1): # max n-1 loops. if update d[] in n-th loop -> negative cycle
        update = False
        for v_from, v_to, cost in g:
            if d[v_from] != INF and d[v_to] > d[v_from] + cost:
                d[v_to] = d[v_from] + cost
                update = True
        if not update:
            break

    for i in range(n-1): # max n-1 loops. if update d[] in n-th loop -> negative cycle
        update = False
        for v_from, v_to, cost in g:
            if d[v_from] != INF and d[v_to] > d[v_from] + cost:
                d[v_to] = -INF
                update = True
        if not update:
            break

    return d
    


n,m,p =map(int, input().split())
g = []
for _ in range(m):
    a,b,c = map(int, input().split())
    c-=p
    g.append((a-1,b-1,-c))


d = bellman_ford(0,n,g)
if d[-1] == -INF: print(-1)
else:
    ans = -d[-1]
    ans = max(0,ans)
    print(ans)