def check(a,b,c,d):
    if d<a or b<c:return False
    return True

n=int(input())
lrs=[]
for _ in range(n):
    t,l,r=map(int, input().split())
    if t==2:r-=0.1
    if t==3:l+=0.1
    if t==4:
        r-=0.1
        l+=0.1
    lrs.append((l,r))
ans=0
for i in range(n):
    a,b=lrs[i]
    for j in range(i+1,n):
        c,d=lrs[j]
        if check(a,b,c,d):ans+=1
# print(lrs)
print(ans)