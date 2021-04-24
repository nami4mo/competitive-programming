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

n,b,k=map(int, input().split())
cl=list(map(int, input().split()))
mat=[[0]*b for _ in range(b)]

for i in range(b):
    for j in range(b):
        for c in cl:
            if (j*10+c)%b==i:mat[i][j]=1

MOD=10**9+7
mat=pow_mat(mat,n,MOD)
ans=mat[0][0]
print(ans)