n=int(input())
xl=[]
yl=[]
for _ in range(n):
    x,y=map(int, input().split())
    xl.append(x)
    yl.append(y)

xl.sort()
yl.sort()

cx=xl[n//2]
cy=yl[n//2]
ans=0
for x in xl:
    ans+=abs(x-cx)
for y in yl:
    ans+=abs(y-cy)
print(ans)