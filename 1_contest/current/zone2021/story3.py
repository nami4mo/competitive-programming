n,m=map(int, input().split())
gl=[[False]*n for _ in range(50)]
for i in range(n): gl[i][i]=True
for _ in range(m):
    a,b=map(int, input().split())
    gl[a][b]=True
    gl[b][a]=True

ans=0
al=[]
for i in range(50):
    for j in range(50):
        for k in range(50):
            val=3
            for l in range(50):
                if gl[l][i] or gl[l][j] or gl[l][k]:val+=1
            if val>ans:
                ans=val
                al=[i,j,k]
print(*al)