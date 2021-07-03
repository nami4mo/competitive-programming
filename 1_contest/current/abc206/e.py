l,r=map(int, input().split())
gl=[0]*(r+1)

for i in range(r,1,-1):
    rcnt=r//i
    lcnt=(l-1)//i
    cnt=rcnt-lcnt
    cnt*=cnt # (l,r) pair
    for bai in range(i+i,r+1,i):
        cnt-=gl[bai]
    gl[i]=cnt
# print(gl)

ans=0
for i in range(2,r+1):
    cnt=gl[i]
    if i>=l:
        cnt-=1 # e.g. (4,4), (6,6)
        rcnt=r//i-1
        baicnt=rcnt
        baicnt*=2
        cnt-=baicnt
    ans+=cnt

print(ans)