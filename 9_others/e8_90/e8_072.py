import sys
sys.setrecursionlimit(10**6)

h,w=map(int, input().split())
sl=[input() for _ in range(h)]
n=h*w
gl=[[] for _ in range(n)]
for y in range(h):
    for x in range(w):
        if sl[y][x]=='#':continue
        pos=y*w+x
        if y!=0 and sl[y-1][x]=='.':
            gl[pos].append(pos-w)
        if y!=h-1 and sl[y+1][x]=='.':
            gl[pos].append(pos+w)
        if x!=0 and sl[y][x-1]=='.':
            gl[pos].append(pos-1)
        if x!=w-1 and sl[y][x+1]=='.':
            gl[pos].append(pos+1)

ans=0
def dfs(pos, start, vis, cnt):
    global ans
    for neib in gl[pos]:
        if neib==start:
            ans=max(ans, cnt)
        if vis[neib]:continue
        vis[neib]=True
        dfs(neib, start, vis, cnt+1)
        vis[neib]=False

for i in range(n):
    vis=[False]*n
    vis[i]=True
    dfs(i,i,vis,1)
    
if ans<3:ans=-1
print(ans)