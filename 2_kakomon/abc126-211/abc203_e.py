n,m=map(int, input().split())
xyl=[]

for _ in range(m):
    x,y=map(int, input().split())
    if y>n+m or y<n-m:continue
    xyl.append((x,y))

xyl.sort()

ds={i:False for i in range(n-m-2,n+m+3)}
ds[n]=True
prev_x=-1
dels=[]
ins=[]
for x,y in xyl:
    if prev_x!=x:
        for v in dels:ds[v]=False
        for v in ins: ds[v]=True
        dels=[]
        ins=[]
    dels.append(y)
    if ds[y-1] or ds[y+1]:ins.append(y)
    prev_x=x
    

for v in dels: ds[v]=False
for v in ins: ds[v]=True
dels=[]
ins=[]
ans=0
for i in range(n-m-2,n+m+3):
    if ds[i]:ans+=1
# print(ds)
print(ans)