def dfs(node,ansl,gl):
    if ansl[node]!=-1:return ansl[node]
    ma=0
    mi=10000000
    cnt=0
    for buka in gl[node]:
        buka_v=dfs(buka,ansl,gl)
        ma=max(ma,buka_v)
        mi=min(mi,buka_v)
        cnt+=1
    if cnt==0:
        ansl[node]=1
        return 1
    else:
        v=ma+mi+1
        ansl[node]=v
        return v

n=int(input())
gl=[[] for _ in range(n)]
for i in range(1,n):
    pare=int(input())
    gl[pare-1].append(i)

ansl=[-1]*n
ans=dfs(0,ansl,gl)
print(ans)
