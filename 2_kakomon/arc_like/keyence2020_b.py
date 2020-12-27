n=int(input())
lrs=[]
for _ in range(n):
    x,l=map(int, input().split())
    lrs.append((x-l,x+l))

lrs.sort(key=lambda x: x[1])
ans=0
cr=-10**10
for l,r in lrs:
    if l<cr:continue
    ans+=1
    cr=r
print(ans)
# print(lrs)