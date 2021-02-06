class Combination:
    def __init__(self, n_max=10**6, mod=10**9+7):
        # self._n_max = n_max
        self._fac, self._finv, self._inv = [0]*n_max, [0]*n_max, [0]*n_max
        self._fac[0], self._fac[1] = 1, 1
        self._finv[0], self._finv[1] = 1, 1
        self._inv[1] = 1
        self._mod = mod
        for i in range(2, n_max):
            self._fac[i] = self._fac[i - 1] * i % self._mod
            self._inv[i] = self._mod - self._inv[self._mod%i] * (self._mod // i) % self._mod
            self._finv[i] = self._finv[i - 1] * self._inv[i] % self._mod
    def com(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self._fac[n] * (self._finv[r] * self._finv[n - r] % self._mod) % self._mod

    def perm(self,n,r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self._fac[n] * (self._finv[n-r] % self._mod) % self._mod

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

MOD = 10**9+7
comb = Combination(10**5+100, MOD)
n,m=map(int, input().split())
sign=n//abs(n)
n=n*sign
facs=p_factorization_t(n)
al=[v for p,v in facs]
ans=1
cnt=0
# print(al)
for a in al:
    ans*=comb.com(a+m-1,m-1)
    ans%=MOD
    cnt+=a
# print(ans)

ansmul=0
if sign==1:
    for mc in range(0,m+1,2):
        ansmul+=comb.com(m,mc)
        ansmul%=MOD
else:
    for mc in range(1,m+1,2):
        ansmul+=comb.com(m,mc)
        ansmul%=MOD
# pm=comb.perm(cnt,cnt)
# mi = modinv(pm,MOD)
# ans = (ans*mi)%MOD
print((ans*ansmul)%MOD)
