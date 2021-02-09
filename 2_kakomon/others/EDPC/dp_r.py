from typing import overload


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
al=[]
for _ in range(n):
    row=list(map(int, input().split()))
    al.append(row)

res=pow_mat(al,k,10**9+7)
ans=0
for row in res:
    for v in row:
        ans+=v
ans%=(10**9+7)
print(ans)