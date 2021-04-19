n=int(input())
xyl0=[]
xyl1=[]
for _ in range(n):
    x,y=map(int, input().split())
    xyl0.append(x+y)
    xyl1.append(x-y)

xyl0.sort()
xyl1.sort()
ans=max(xyl0[-1]-xyl0[0], xyl1[-1]-xyl1[0])
print(ans)