n=int(input())
xyl=[]
st=set()
MAX=10**9+1

for _ in range(n):
    x,y=list(map(int, input().split()))
    xyl.append((x,y))
    st.add((x,y))

ans=0
for i in range(n-1):
    xi,yi=xyl[i]
    for j in range(i+1,n):
        xj,yj=xyl[j]
        if xi==xj or yi==yj:continue
        if (xi,yj) in st and (xj,yi) in st:
            ans+=1
            # print(xi,yi,xj,yj)
print(ans//2)   