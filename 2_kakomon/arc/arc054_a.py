l,x,y,s,d=map(int, input().split())
dist1=(d-s)%l
ans1=dist1/(x+y)
if y-x>0:
    dist2=(s-d)%l
    ans2=dist2/(y-x)
    print(min(ans1,ans2))
else:
    print(ans1)
    