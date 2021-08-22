''' 行列累乗 '''
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

def modinv(a,m):
    b, u, v = m, 1, 0
    while b:
        t = a//b
        a -= t*b
        a,b = b,a
        u -= t * v
        u,v = v,u
    u %= m
    return u

n,m,k=map(int, input().split())
al=list(map(int, input().split()))
gl=[[] for _ in range(n)]
for _ in range(m):
    x,y=map(int, input().split())
    x-=1
    y-=1
    gl[x].append(y)
    gl[y].append(x)

MOD=10**9+7
mat=[[0]*n for _ in range(n)]

minv=modinv(m,MOD)
m2inv=modinv(2*m,MOD)

for i in range(n):
    v=0
    # not chosen
    elen=len(gl[i])
    notelen=m-elen
    v+=notelen*minv
    # chosen
    v+=elen*m2inv
    mat[i][i]=v%MOD
    for neib in gl[i]:
        mat[i][neib]=(1*m2inv)%MOD
    
# print(mat)
matk=pow_mat(mat,k,MOD)
# print(matk)
ansl=[]
for i in range(n):
    v=0
    row=matk[i]
    for j in range(n):
        v+=row[j]*al[j]
    ansl.append(v%MOD)
for a in ansl:print(a)