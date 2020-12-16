def multi_mat(x,y,mod):
    res = [[0,0],[0,0]]
    res[0][0] = x[0][0]*y[0][0]+x[0][1]*y[1][0]
    res[0][1] = x[0][0]*y[0][1]+x[0][1]*y[1][1]
    res[1][0] = x[1][0]*y[0][0]+x[1][1]*y[1][0]
    res[1][1] = x[1][0]*y[0][1]+x[1][1]*y[1][1]
    for i in range(2):
        for j in range(2):
            res[i][j]%=mod
    return res

def pow_mat(x,n,mod): 
    res = [[1,0],[0,1]]
    if n == 0: return res
    xk = x
    while n > 1:
        if n%2 != 0:
            res = multi_mat(res,xk,mod)
        xk = multi_mat(xk,xk,mod)
        n >>= 1
    return multi_mat(res,xk,mod) 


n=int(input())
al=[]
for _ in range(n):
    a,l=map(int, input().split())
    al.append((a,l))
m=int(input())

rem = 0
for a,l in al:
    keta = len(str(a))
    x=[[10**keta,a],[0,1]]
    mat_k=pow_mat(x,l,m)
    rem=mat_k[0][0]*rem+mat_k[0][1]
    rem%=m
print(rem)