
n=int(input())
xyl=[]
for _ in range(n):
    x,y=map(int, input().split())
    xyl.append((x,y))

ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            dx1 = xyl[i][0]-xyl[j][0]
            dy1 = xyl[i][1]-xyl[j][1]
            dx2 = xyl[i][0]-xyl[k][0]
            dy2 = xyl[i][1]-xyl[k][1]
            s2 = abs(dx1*dy2-dx2*dy1)
            if s2 > 0 and s2%2 == 0: ans+=1

print(ans)