n=int(input())
aal=list(map(int, input().split()))
al=[]
bl=[]
k=0
emp=0
for i in range(n):
    if aal[i]==0:
        bl.append(i)
        emp+=1
    else:
        al.append(i)
        k+=1

if k==0:
    print(0)
    exit()

dp=[[10**10]*(emp+1) for _ in range(k+1)]
dp[0][0]=0
for i in range(1,k+1):
    a=al[i-1]
    mi=10**10
    val_mi=10**10
    for j in range(i,emp+1):
        b=bl[j-1]
        mi=min(mi, dp[i-1][j-1])
        val_mi=min(mi+abs(a-b), val_mi)
        dp[i][j]=val_mi

print(dp[k][emp])
# print(dp)