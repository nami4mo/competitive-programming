n,m=map(int, input().split())
bl=[]
for _ in range(n):
    row=list(map(int, input().split()))
    bl.append(row)

ok=True
top=bl[0]
for i in range(m):
    if i==0:
        if top[i]%7==0:
            ok=False
    else:
        if (not ok) or top[i]-top[i-1]!=1:
            print('No')
            exit()
        if top[i]%7==0:
            ok=False

for j in range(m):
    for i in range(n-1):
        if bl[i+1][j]-bl[i][j]!=7:
            print('No')
            exit()
print('Yes')
