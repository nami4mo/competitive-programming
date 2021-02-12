n=int(input())
xyl=[]
for _ in range(n):
    x,y=map(int, input().split())
    xyl.append((x,y))

xyl.sort()
ans=0
for i in range(n):
    for j in range(i+1,n):
        x1,y1=xyl[i]
        x2,y2=xyl[j]
        dx=x2-x1
        dy=y2-y1
        if abs(dx)>=abs(dy):ans+=1
print(ans)