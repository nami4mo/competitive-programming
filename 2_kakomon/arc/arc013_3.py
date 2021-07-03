n=int(input())
val=0
for _ in range(n):
    X,Y,Z=map(int, input().split())
    xmi,xma=10**10,-1
    ymi,yma=10**10,-1
    zmi,zma=10**10,-1
    for m_ in range(int(input())):
        x,y,z=map(int, input().split())
        xma=max(xma,x)
        xmi=min(xmi,x)
        yma=max(yma,y)
        ymi=min(ymi,y)
        zma=max(zma,z)
        zmi=min(zmi,z)
    val^=xmi
    val^=ymi
    val^=zmi
    val^=(X-1-xma)
    val^=(Y-1-yma)
    val^=(Z-1-zma)

if val==0:
    print('LOSE')
else:
    print('WIN')
