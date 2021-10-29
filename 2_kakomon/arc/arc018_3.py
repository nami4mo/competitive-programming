n,m=map(int, input().split())
x,a,p=map(int, input().split())
xl=[x]
for i in range(n*m-1):
    xl.append((xl[-1]+a)%p)
xl=[(x,i) for i,x in enumerate(xl)]
xl.sort(key=lambda x:x[0])

ans=0
for i in range(n):
    cl=xl[i*m:(i+1)*m]
    dl=[]
    for _,pos in cl:
        y=pos//m
        x=pos%m
        ans+=abs(y-i)
        dl.append(x)
    dl.sort()
    for j,d in enumerate(dl):
        ans+=abs(j-d)
print(ans)
