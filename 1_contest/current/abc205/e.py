
# # n,m,k=map(int, input().split())
# dp={0:1}

# k=5
# for i in range(10):
#     new_dp={}
#     for key,v in dp.items():
#         if key>k:continue
#         new_dp.setdefault(key-1,0)
#         if key+1<=k:new_dp.setdefault(key+1,0)
#         new_dp[key-1]+=v
#         if key+1<=k:new_dp[key+1]+=v
#     l=[]
#     for key,v in new_dp.items():
#         dp[key]=v
#         l.append((key,v))
#     # print(dp)
#     l.sort()
#     print(l)
#     # for _,v in l:
#         # print(v)

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

    def lucas(self, n, r): # nCr (mod self._mod(prime)) 
        if n < r: return 0 
        res = 1
        while n > 0:
            nq, rq = n//self._mod, r//self._mod
            nr, rr = n-nq*self._mod, r-rq*self._mod
            res *= self.com(nr, rr)
            res %= self._mod
            n, r = nq, rq
        return res

MOD = 10**9+7
comb = Combination(2*10**6+1, MOD)

n,m,k=map(int, input().split())
notpat=0
koepat=0
min_koeru=k+1

if n-m>k:
    print(0)
    exit()

for i in range(1, n+m+1): # iで初めて超える
    # print('---',i)

    if (k+i-1)%2==1:continue
    koepat*=2
    koepat%=MOD
    a=(k+i-1)//2
    b=i-1-a
    # print(a,b)
    # if a>n or b>m:continue
    if not (0<=a<=n-1 and 0<=b<=m):continue
    prev=comb.com(i-1,a)-koepat # i-1 で k 
    koepat+=prev
    rem_a=n-a-1
    rem_b=m-b
    rem_pat=comb.com(rem_a+rem_b, rem_a)
    i_koe_pat=prev*rem_pat
    i_koe_pat-=notpat
    # print(prev)
    # print(rem_pat)
    # print(i_koe_pat)   
    if i_koe_pat<0:continue
    notpat+=i_koe_pat
    notpat%=MOD

    # print(i_koe_pat)
    # print(notpat)

allpat=comb.com(n+m,n)
ans=allpat-notpat
ans%=MOD
print(ans)