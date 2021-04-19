r,c,d=map(int, input().split())
al=[list(map(int, input().split())) for _ in range(r)]
ans=0
for y in range(r):
    for x in range(c):
        if y+x<=d and (y+x)%2==d%2:
            ans=max(ans,al[y][x])
print(ans)