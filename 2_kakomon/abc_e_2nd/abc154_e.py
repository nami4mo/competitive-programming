n=input()
ln=len(n)
k=int(input())

dp_same=[[0]*(k+2) for _ in range(ln+1)]
dp_small=[[0]*(k+2) for _ in range(ln+1)]
dp_same[0][0]=1

for i in range(ln):
    ni=int(n[i])
    for j in range(k+1):
        if ni==0:
            dp_same[i+1][j]+=dp_same[i][j]
            dp_small[i+1][j]+=dp_small[i][j]
            dp_small[i+1][j+1]+=dp_small[i][j]*9
        else:
            # choose 1~
            dp_same[i+1][j+1]+=dp_same[i][j]
            dp_small[i+1][j+1]+=dp_same[i][j]*(ni-1)
            dp_small[i+1][j+1]+=dp_small[i][j]*9

            # choose 0
            dp_small[i+1][j]+=dp_same[i][j]
            dp_small[i+1][j]+=dp_small[i][j]


# print(dp_same)
# print(dp_small)
ans=dp_same[ln][k]+dp_small[ln][k]
print(ans)