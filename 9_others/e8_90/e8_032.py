n=int(input())
al=[list(map(int, input().split())) for _ in range(n)]
gl=[[True]*n for _ in range(n)]
for _ in range(int(input())):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a][b]=False
    gl[b][a]=False

from itertools import permutations
ll = list(range(n))  # list of elements
perml = list(permutations(ll, n))

INF=10**18
ans=INF
for perm in perml:
    val=0
    for i in range(n):
        if i!=n-1 and not gl[perm[i]][perm[i+1]]:break
        val+=al[perm[i]][i]
    else:
        ans=min(ans,val)
if ans==INF:ans=-1
print(ans)