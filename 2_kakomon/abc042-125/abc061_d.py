'''
    [bellman_ford]
'''
def bellman_ford(s, n, g): # s: start, n: |V|, g; glaph 
    INF = 10**18
    d = [INF]*n
    d[s] = 0
    for i in range(n-1): # max n-1 loops. if update d[] in n-th loop -> negative cycle
        update = False
        for v_from, v_to, cost in g:
            if d[v_to] > d[v_from] + cost:
                d[v_to] = d[v_from] + cost
                update = True
        if not update:
            return d
    return d
    # else: # if not break until n-th loop -> detect negative cycle
    #     # may do something for negatice cycle
    #     return None


def bellman_ford2(s, n, g, d): # s: start, n: |V|, g; glaph 
    INF = 10**18
    # d = [INF]*n
    # d[s] = 0
    for i in range(n-1): # max n-1 loops. if update d[] in n-th loop -> negative cycle
        update = False
        for v_from, v_to, cost in g:
            if d[v_to] > d[v_from] + cost:
                d[v_to] = -INF
    return d


n,m = map(int, input().split())
g = []
for _ in range(m):
    a,b,c = map(int, input().split())
    g.append((a-1,b-1,-c))

d = bellman_ford(0,n,g)
d2 = bellman_ford2(0,n,g,d[:])

INF = 10**18
if d2[n-1] <= -INF:
    print('inf')
else:
    print(-d[n-1])