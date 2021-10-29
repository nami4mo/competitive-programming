n=int(input())
xyl=[]
for _ in range(n):
    x,y=map(int, input().split())
    xyl.append((x,y))
xyl.sort()
ans=0
for i in range(n):
    x1,y1=xyl[i]
    for j in range(i+1,n):
        x2,y2=xyl[j]
        for k in range(j+1,n):
            x3,y3=xyl[k]
            dx1=x2-x1
            dy1=y2-y1
            dx2=x3-x2
            dy2=y3-y2
            if dx1*dy2!=dy1*dx2:ans+=1

print(ans)