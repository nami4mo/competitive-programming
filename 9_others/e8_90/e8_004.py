h,w=map(int, input().split())
al=[list(map(int, input().split())) for _ in range(h)]
hsum=[0]*h
wsum=[0]*w
for i in range(h):
    for j in range(w):
        hsum[i]+=al[i][j]
        wsum[j]+=al[i][j]

for i in range(h):
    bl=[]
    for j in range(w):
        b=hsum[i]+wsum[j]-al[i][j]
        bl.append(b)
    print(*bl)