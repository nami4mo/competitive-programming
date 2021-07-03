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


def get_pat(c):
    if c==6: return 13
    if c==5: return 8
    if c==4: return 5
    if c==3: return 3
    if c==2: return 2
    if c==1: return 1


h,w=map(int, input().split())
MAX=(1<<h)
gl=[[0]*MAX for _ in range(MAX)]

for i in range(MAX):
    al=[]
    for j in range(h):
        if i&(1<<j):al.append(True)
        else:al.append(False)

    for j in range(MAX):
        # print('---',i,j)
        pat=1
        rem=[0]*h
        if i&j: continue
        for k in range(h):
            if j&(1<<k)==0 and (not al[k]):
                rem[k]=1

        cntl = []
        prev = rem[0]
        cnt = 1
        for a in rem[1:]:
            if prev == a: cnt+=1
            else:
                cntl.append((prev,cnt))
                cnt = 1
                prev = a
        cntl.append((prev,cnt))
        # print(cntl)
        for val,cnt in cntl:
            if val==0:continue
            pat*=get_pat(cnt)
        gl[i][j]=pat

# print(gl)
MOD=998244353
dp=[0]*MAX
dp[0]=1
pmat=pow_mat(gl,w,MOD)
print(pmat[0][0]%MOD)