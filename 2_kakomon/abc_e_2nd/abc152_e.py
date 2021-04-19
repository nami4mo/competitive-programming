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

def p_factorization_t(n):
    if n == 1: return []
    pf_cnt = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            pf_cnt.append((i,cnt))

    if temp != 1: pf_cnt.append((temp,1))
    return pf_cnt

n=int(input())
al=list(map(int, input().split()))
lcml={}
pfl=[]
for a in al:
    pf=p_factorization_t(a)
    for k,v in pf:
        lcml.setdefault(k,0)
        lcml[k]=max(lcml[k],v)
    pfl.append(pf)

lcm=1
MOD=10**9+7
for k,v in lcml.items():
    lcm*=pow(k,v,MOD)
    lcm%=MOD

ans=0
for a in al:
    v=lcm*modinv(a,MOD)
    ans+=v
    ans%=MOD
print(ans)