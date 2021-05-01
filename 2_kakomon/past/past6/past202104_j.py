n,c=map(int, input().split())
v=0
xl=[]
xsum=0
for _ in range(n):
    x,y=map(int, input().split())
    v+=(y-c)**2
    xl.append(x)
    xsum+=x

minx=xsum/n
for x in xl:
    v+=(minx-x)**2
print(v)