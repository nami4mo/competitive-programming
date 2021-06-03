n,D,H=map(int, input().split())
minxy=10**10
for _ in range(n):
    d,h=map(int, input().split())
    dy=H-h
    dx=D-d
    minxy=min(minxy,dy/dx)

dy=D*minxy
ans=H-dy
if ans<0:ans=0
print(ans)