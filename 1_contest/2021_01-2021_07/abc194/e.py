n,m=map(int, input().split())
d=[[-1] for _ in range(n)]

al=list(map(int, input().split()))
for i,a in enumerate(al):
    d[a].append(i)

for a in range(n):
    d[a].append(n)
    ok=False
    for i in range(len(d[a])-1):
        if d[a][i+1]-d[a][i]>m:
            print(a)
            exit()
print(n)