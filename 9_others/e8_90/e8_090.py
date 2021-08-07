def multi_mat(x,y,mod):
    row=len(x)
    mid=len(y) # len(x[0])
    col=len(y[0])
    res=[[0]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            for k in range(mid):
                res[i][j]+=x[i][k]*y[k][j]
            res[i][j]%=mod
    return res

def pow_mat(x,n,mod): 
    size=len(x)
    res=[[0]*size for _ in range(size)]
    for i in range(size): res[i][i]=1
    if n == 0: return res
    xk = x
    while n > 1:
        if n%2 != 0:
            res = multi_mat(res,xk,mod)
        xk = multi_mat(xk,xk,mod)
        n >>= 1
    return multi_mat(res,xk,mod) 


n,k=map(int, input().split())
MOD=998244353
if k==1:
    if n==1:
        print(2)
    else:
        x=[[1,1],[1,0]]
        mat=pow_mat(x,n-1,MOD)
        ans=mat[1][0]*3+mat[1][1]*2
        print(ans%MOD)
    exit()

if n>10000 or k>10000:
    exit()

dp=[0]*(k+1)
dp[0]=1

for num in range(k,-1,-1):
    if num==0:
        max_len=n
    else:
        max_len=k//num
    new_dp=[0]*(max_len+2)
    new_dp[0]=1
    added=[0]*(max_len+2)

    dplen=len(dp)
    for i in range(max_len):
        for j in range(max_len+1):
            if i+j+1==max_len+1:
                if j!=0:
                    # print(i,j,added,dp)
                    if j>=dplen:continue
                    added[i+j]+=new_dp[i]*dp[j]
                    added[i+j]%=MOD
                continue
            if i+j+1>max_len+1:break
            if j<dplen:
                new_dp[i+j+1]+=new_dp[i]*dp[j]
                new_dp[i+j+1]%=MOD
            if j!=0:
                if j<dplen:
                    added[i+j]+=new_dp[i]*dp[j]
                    added[i+j]%=MOD
    for j in range(max_len+1):
        new_dp[j]+=added[j]
    dp=new_dp[:]

print(dp[n]%MOD)


# dp2=[0]*(n+1)
# dp2[0]=1
# ans=0
# for i in range(n):
#     for j in range(k+1): # 長さjの列を使う
#         if i+j+1==n+1:
#             ans+=dp2[i]*dp[j]
#             ans%=MOD
#             break
#         dp2[i+j+1]+=dp2[i]*dp[j]
#         dp2[i+j+1]%=MOD
# ans+=dp2[-1]
# ans%=MOD
# print(ans)
