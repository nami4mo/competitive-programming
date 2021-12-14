n,a,b=map(int, input().split())
p,q,r,s=map(int, input().split())

k1=max(1-a,1-b)
k2=min(n-a,n-b)

k3=max(1-a,b-n)
k4=min(n-a,b-1)

ans=[]
for y in range(p,q+1):
    row=[]
    for x in range(r,s+1):
        ok=False
        if a-b==y-x:
            d=y-a
            if k1<=d<=k2:
                ok=True
        da=y-a
        db=x-b
        if da==db*(-1):
            if k3<=da<=k4:
                ok=True
        if ok:row.append('#')
        else:row.append('.')
    print(''.join(row))