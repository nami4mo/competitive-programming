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

MOD=998244353
comb = Combination(10**5, MOD)
k,n=map(int, input().split())

ansl=[]
for i in range(2,k+2):
# for i in range(2,2*k+1):
    double=0
    if i%2==0: double=1
    pair=(i-1)//2
    nums=pair*2+double
    ans=0
    if not double:
        for use_p in range(0,pair+1):
            cnt=n-use_p
            if cnt<0:continue
            types=k-nums+use_p
            ans+=comb.com(cnt+types-1,types-1)*pow(2,use_p,MOD)*comb.com(pair,use_p)
            ans%=MOD
            # print(use_p,ans)
    else:
        for use_p in range(0,pair+1):
            cnt=n-use_p
            if cnt<0:continue
            types=k-nums+use_p
            ans+=comb.com(cnt+types-1,types-1)*pow(2,use_p,MOD)*comb.com(pair,use_p)
            ans%=MOD
        for use_p in range(0,pair+1):
            cnt=(n-1)-use_p
            if cnt<0:continue
            types=k-nums+use_p
            ans+=comb.com(cnt+types-1,types-1)*pow(2,use_p,MOD)*comb.com(pair,use_p)
            ans%=MOD
    # print(ans)
    ansl.append(ans)

revs=ansl[:-1]
revs=revs[::-1]
ansl+=revs
for a in ansl:print(a)