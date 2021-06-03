n,m=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))

d={}
for i in range(n):
    for j in range(m):
        v=al[i]+bl[j]
        if v in d:
            x,y=d[v]
            print(x,y,i,j)
            exit()
        d[v]=(i,j)
print(-1)