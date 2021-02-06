def multi_mat(x,y,mod):
    res = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                res[i][j]+=x[i][k]*y[k][j]
            res[i][j]%=mod
    return res

def pow_mat(x,n,mod): 
    res = [[1,0,0],[0,1,0],[0,0,1]]
    if n == 0: return res
    xk = x
    while n > 1:
        if n%2 != 0:
            res = multi_mat(res,xk,mod)
        xk = multi_mat(xk,xk,mod)
        n >>= 1
    return multi_mat(res,xk,mod) 


l,a,b,m=map(int, input().split())

prev_keta_end=-1
keta_min=len(str(a))
ans=0
for keta in range(keta_min, 20):

    keta_start=prev_keta_end+1
    keta_end=(pow(10,keta)-a-1)//b
    keta_end=min(keta_end,l-1)
    keta_n=keta_end-keta_start+1

    if keta_end<keta_start:continue

    x=[[pow(10,keta,m),1,0],[0,1,b],[0,0,1]]
    xk=pow_mat(x,keta_n-1,m)
    x0=a+keta_start*b
    a0=x0+b
    xi=xk[0][0]*x0+xk[0][1]*a0+xk[0][2]

    up=pow(10,keta*keta_n,m)
    ans*=up
    ans%=m
    ans+=xi
    ans%=m
    prev_keta_end=keta_end

print(ans)