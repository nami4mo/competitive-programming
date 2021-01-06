d=int(input())
n=input()

dp_same=[[0]*d for _ in range(len(n)+1)]
dp_small=[[0]*d for _ in range(len(n)+1)]
dp_same[0][0]=1
MOD=10**9+7
for i in range(len(n)):
    ni = int(n[i])
    for j in range(d):
        dp_same[i+1][(j+ni)%d] += dp_same[i][j]
        dp_same[i+1][(j+ni)%d]%=MOD
        for v in range(10):
            if v<ni:
                dp_small[i+1][(j+v)%d] += dp_same[i][j]
            dp_small[i+1][(j+v)%d] += dp_small[i][j]
            dp_small[i+1][(j+v)%d]%=MOD

print((dp_small[-1][0]+dp_same[-1][0]-1)%MOD)