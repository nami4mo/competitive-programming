h,w=map(int, input().split())
al=[list(map(int, input().split())) for _ in range(h)]
bl=[list(map(int, input().split())) for _ in range(h)]

ans=0
for y in range(h-1):
    for x in range(w-1):
        d=bl[y][x]-al[y][x]
        al[y][x]+=d
        al[y+1][x]+=d
        al[y][x+1]+=d
        al[y+1][x+1]+=d
        ans+=abs(d)

for y in range(h):
    for x in range(w):
        if al[y][x]!=bl[y][x]:
            print('No')
            exit()
print('Yes')
print(ans)