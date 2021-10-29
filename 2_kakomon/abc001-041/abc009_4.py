''' 行列累乗 '''
def multi_mat(x,y,mod):
    row=len(x)
    mid=len(y) # len(x[0])
    col=len(y[0])
    res=[[0]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            for k in range(mid):
                res[i][j]^=x[i][k]&y[k][j]
    return res

def pow_mat(x,n,mod): 
    size=len(x)
    res=[[0]*size for _ in range(size)]
    for i in range(size): res[i][i]=pow(2,32)-1
    if n == 0: return res
    xk = x
    while n > 1:
        if n%2 != 0:
            res = multi_mat(res,xk,mod)
        xk = multi_mat(xk,xk,mod)
        n >>= 1
    return multi_mat(res,xk,mod) 



def solve(k,m,al,cl):
    if len(al)>=m:
        return al[m-1]
    mat=[]
    for i in range(k-1):
        row=[0]*k
        row[i+1]=pow(2,32)-1
        mat.append(row)
    mat.append(cl[::-1])
    mat=pow_mat(mat,m-1,2)
    res=0
    for i in range(k):
        res^=mat[0][i]&al[i]
    return res

k,m=map(int, input().split())
al=list(map(int, input().split()))
cl=list(map(int, input().split()))
ans=solve(k,m,al,cl)
print(ans)

# for bit in range(32):
#     aal=[]
#     ccl=[]
#     for i in range(k):
#         if al[i]&(1<<bit)>0:aal.append(1)
#         else: aal.append(0)
#         if cl[i]&(1<<bit)>0:ccl.append(1)
#         else: ccl.append(0)
#     res=solve(k,m,aal,ccl)
#     if res==1:
#         ans+=(1<<bit)
# print(ans)