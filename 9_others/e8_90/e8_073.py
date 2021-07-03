import sys
sys.setrecursionlimit(10**6)

n=int(input())
cl=list(map(str, input().split()))
gl=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)


MOD=10**9+7
def dfs(node,pare):
    bl,rl,brl=[],[],[]
    for neib in gl[node]:
        if neib==pare:continue
        b,r,br=dfs(neib,node)
        bl.append(b)
        rl.append(r)
        brl.append(br)
    res_r=0
    res_b=0
    res_br=0
    allcnt=1
    if cl[node]=='b':
        res_b=1
        for b,r,br in zip(bl,rl,brl):
            res_b*=(b+br)
            allcnt*=(b+r+br*2)
            res_b%=MOD
            allcnt%=MOD
        res_br=allcnt-res_b
    else:
        res_r=1
        for b,r,br in zip(bl,rl,brl):
            res_r*=(r+br)
            allcnt*=(b+r+br*2)
            res_r%=MOD
            allcnt%=MOD
        res_br=allcnt-res_r
    return res_b%MOD,res_r%MOD,res_br%MOD

b,r,br=dfs(0,-1)
print(br)
