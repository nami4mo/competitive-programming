# n=int(input())
# cnts=[0]*n
# gl=[[] for _ in range(n)]
# for _ in range(n-1):
#     a,b=map(int, input().split())
#     a-=1
#     b-=1
#     gl[a].append(b)
#     gl[b].append(a)
#     cnts[a]+=1
#     cnts[b]+=1

# cc=[(c,i) for i,c in enumerate(cnts)]
# cc.sort()

# used=[False]*n
# cnt=0
# al=[]
# for _,i in cc:
#     if used[i]:continue
#     cnt+=1
#     used[i]=True
#     for neib in gl[i]:
#         used[neib]=True
#     al.append(i+1)
#     if cnt==n//2:break

# print(*al)

import sys
sys.setrecursionlimit(10**6)

n=int(input())
gl=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

used=[False]*n
ansl=[]

def dfs(node,pare,used,ansl,gl):
    ok=True
    for neib in gl[node]:
        if neib==pare:
            if used[pare]:ok=False
        else:
            res=dfs(neib,node,used,ansl,gl)
            if res: ok=False
    if ok:
        ansl.append(node+1)
        used[node]=True
    return ok

dfs(0,-1,used,ansl,gl)
print(*ansl[:n//2])