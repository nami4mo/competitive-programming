n=int(input())
xl=[]
yl=[]
for i in range(n):
    x,y=map(int, input().split())
    xl.append((x,i))
    yl.append((y,i))

xl.sort()
yl.sort()

x1=xl[-1][0]-xl[0][0]
y1=yl[-1][0]-yl[0][0]

xinds=[xl[-1][1],xl[0][1]]
yinds=[yl[-1][1],yl[0][1]]
xinds.sort()
yinds.sort()
# if xinds != yinds:
#     print(min(x1,y1))
#     exit()

x2=xl[-1][0]-xl[1][0]
x3=xl[-2][0]-xl[0][0]
y2=yl[-1][0]-yl[1][0]
y3=yl[-2][0]-yl[0][0]

if xinds == yinds:
    print(max(x2,x3,y2,y3))

else:
    if x1>y1:
        print(max(y1,x2,x3,y2,y3))
    else:
        print(max(x1,x2,x3,y2,y3))
