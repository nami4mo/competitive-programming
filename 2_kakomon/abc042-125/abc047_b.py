w,h,n=map(int, input().split())
lx,rx=0,w
ly,ry=0,h
for _ in range(n):
    x,y,a=map(int, input().split())
    if a==1:lx=max(lx,x)
    if a==2:rx=min(rx,x)
    if a==3:ly=max(ly,y)
    if a==4:ry=min(ry,y)

x=max(0,rx-lx)
y=max(0,ry-ly)
ans=x*y
print(ans)
# print(lx,rx)
# print(ly,ry)
