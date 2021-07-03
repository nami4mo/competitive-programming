n,k=map(int, input().split())
MOD=10**5
MAX=65

db=[[-1]*(MOD+1) for _ in range(MAX)]
for i in range(MOD+1):
    val=i
    for si in str(i):
        val+=int(si)
    val%=MOD
    db[0][i]=val


for i in range(MAX-1):
    for j in range(MOD+1):
        db[i+1][j]=db[i][db[i][j]]

v=n
for i in range(MAX-1):
    if k&(1<<i):
        v=db[i][v]

print(v)
