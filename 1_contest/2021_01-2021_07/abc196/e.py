n=int(input())
# atl=[]
cmax=10**9
cmin=-(10**9)
cadd=0

vmax=10**9
vmin=-(10**9)
for _ in range(n):
    a,t=map(int, input().split())
    if t==1:
        cadd+=a
        vmax+=a
        vmin+=a
    elif t==2:
        cmin=max(cmin, a-cadd)
        vmin=max(vmin, a)
        vmax=max(vmax, a)
    elif t==3:
        cmax=min(cmax, a-cadd)
        vmax=min(vmax, a)
        vmin=min(vmin, a)


q=int(input())
xl=list(map(int, input().split()))
for x in xl:
    if cmin<=x<=cmax:
        print(x+cadd)
    elif x<cmin:
        print(vmin)
    else:
        print(vmax)
