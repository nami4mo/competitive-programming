n=int(input())
al=[]
xsum=0
ysum=0
for _ in range(n):
    x,y=map(int, input().split())
    al.append((x,y))
    xsum+=x
    ysum+=y
agx=xsum/n
agy=ysum/n

bl=[]
xsum=0
ysum=0
for _ in range(n):
    x,y=map(int, input().split())
    bl.append((x,y))
    xsum+=x
    ysum+=y
bgx=xsum/n
bgy=ysum/n

amax2=0
for x,y in al:
    d2=(agx-x)**2+(agy-y)**2
    amax2=max(amax2,d2)

bmax2=0
for x,y in bl:
    d2=(bgx-x)**2+(bgy-y)**2
    bmax2=max(bmax2,d2)

p=bmax2/amax2
ans=p**0.5
print(ans)