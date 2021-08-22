import sys
input = sys.stdin.readline


''' [for DFS] '''
sys.setrecursionlimit(10**6)

n=int(input())
gl=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

for i in range(n):
    gl[i].sort()

ans=[]
def dfs(pare, node):
    # print(node)
    ans.append(node+1)
    # flag=False
    for neib in gl[node]:
        if neib==pare:continue
        # flag=True
        dfs(node, neib)
        ans.append(node+1)
    # print(node+1)
dfs(-1,0)
print(*ans)