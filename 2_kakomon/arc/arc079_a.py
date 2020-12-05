n,m=map(int, input().split())
neibs = []
to_n = [False]*n
for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    if a>b: a,b=b,a
    if b==n-1: to_n[a]=True
    if a==0: neibs.append(b)


for neib in neibs:
    if to_n[neib]:
        print('POSSIBLE')
        break
else:
    print('IMPOSSIBLE')