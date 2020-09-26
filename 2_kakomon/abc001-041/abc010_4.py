from atcoder.maxflow import MFGraph

n, _, e = map(int, input().split())
pl = list(map(int, input().split()))
g = MFGraph(n+1)
for _ in range(e):
    a,b = map(int, input().split())
    g.add_edge(a,b,1)
    g.add_edge(b,a,1)
for p in pl:
    g.add_edge(p,n,1)

ans = g.flow(0,n)
print(ans)