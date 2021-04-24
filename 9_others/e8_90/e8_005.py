n,b,k=map(int, input().split())
cl=list(map(int, input().split()))

db=[[0]*b for _ in range(60)]
for c in cl:
    db[0][c%b]+=1

p2=[10%b]
for i in range(1,60):
    p2.append((p2[-1]**2)%b)

MOD=10**9+7
for i in range(1,60):
    for j in range(b):
        for k in range(b):
            rem=(p2[i-1]*j+k)%b
            db[i][rem]+=db[i-1][j]*db[i-1][k]
            db[i][rem]%=MOD

ansd=[0]*b
first=True
for i in range(0,60):
    if n&(1<<i)==0:continue
    if first:
        ansd=db[i][:]
        first=False
        continue
    new_ansd=[0]*b
    for j in range(b):
        for k in range(b):
            rem=(p2[i]*j+k)%b
            new_ansd[rem]+=ansd[j]*db[i][k]
            new_ansd[rem]%=MOD
    ansd=new_ansd[:]
print(ansd[0])