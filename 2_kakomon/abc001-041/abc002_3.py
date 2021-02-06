x1,y1,x2,y2,x3,y3=map(int, input().split())
dx1=x2-x1
dx2=x3-x1
dy1=y2-y1
dy2=y3-y1
ans=abs(dx1*dy2-dx2*dy1)/2
print(ans)