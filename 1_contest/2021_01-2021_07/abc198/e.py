import sys
sys.setrecursionlimit(10**7)

def dfs(node, pare, cnts, gl, cl, ansl):
    for neib in gl[node]:
        if neib==pare:continue
        c=cl[neib]
        if cnts[c]==0:ansl.append(neib)
        cnts[cl[neib]]+=1
        dfs(neib,node,cnts,gl,cl,ansl)
    cnts[cl[node]]-=1

n=int(input())
cl=list(map(int, input().split()))
gl=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

cnts=[0]*(10**5+1)
cnts[cl[0]]=1
al=[0]

dfs(0,-1,cnts,gl,cl,al)
al.sort()
for a in al:print(a+1)