from atcoder.mincostflow import MCFGraph
INF = 10**18

n,k = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(n)]

g = MCFGraph(n*2+2)
g.add_edge(n*2,n*2+1,n*k,INF)

for i in range(n):
    g.add_edge(n*2,i,k,0)

for i in range(n,n*2):
    g.add_edge(i,n*2+1,k,0)

print(INF)
for i in range(n):
    for j in range(n,n*2):
        g.add_edge(i,j,1,INF-al[i][j-n])
    
cap, cost = g.flow(n*2,n*2+1,n*k)
ans = INF*(n*k) - cost

el = g.edges()
ansl = [ ['.']*n for _ in range(n) ]
for e in el:
    if e.flow > 0 and e.src < n*2 and e.dst < n*2:
        ansl[e.src][e.dst-n] = 'X'


print(ans)
for row in ansl:
    print(''.join(row))