## bit all search
N = 10
for i in range(2 ** N):
    comb = []
    for j in range(N):
        if ((i >> j) & 1): 
            comb.append(j)
    print(comb)


## bit all search (rapid)
from itertools import product
pattern = 2
n = 10
ite = product(range(pattern),repeat=n)
for it in ite:
    comb = []
    for i,j in enumerate(reversed(it)):
        if j == 1:
            comb.append(i)


## k-base all search
# (0,0,0,0,0), (0,0,0,0,1), (0,0,0,0,2), (0,0,0,1,0), ...., (2,2,2,2,2)
from itertools import product
pattern = 3
n = 5
ite = product(range(pattern),repeat=n)
for it in ite:
    pass


from itertools import permutations
n = 5
cl = list(range(1,n+1))
cpl = list(permutations(cl,3))
# [1,2,3],[1,2,4],[1,2,5],[1,3,2],...[5,4,3]


# nCk ( O(N) )
N_MAX = 10**6
MOD = 10**9 + 7
fac, finv, inv = [0]*N_MAX ,[0]*N_MAX, [0]*N_MAX
def com_init():
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, N_MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

def com(n, k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


# nCk (k<=10^7, n<=10^9)
K_MAX = 10**7
MOD = 10**9 + 7
fac, finv, inv = [0]*(K_MAX+1), [0]*(K_MAX+1), [0]*(K_MAX+1)
def com_init():
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2,K_MAX+1):
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

def com(n, k):
    ans = 1
    for i in range(n-k+1,n+1):
        ans *= i
        ans %= MOD
    return (ans * finv[k]) % MOD

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())





class Combination():
    def __init__(self, n, mod):
        self.n = n
        self.mod = mod
        self.fact = self.make_fact(n)
        self.fact_inv = self.make_fact_inv(n)
    def make_fact(self, n):#0~nの階乗を求める
        res = [1]*(n+1)
        for i in range(1, n+1):
            res[i] = res[i-1]*i%self.mod
        return res
    def make_fact_inv(self, n):#0~nの階乗のmodに関する逆元を求める
        fact_inv = [1]*(n+1)
        fact_inv[n] = pow(self.fact[n], self.mod-2, self.mod)#フェルマーの小定理
        for i in range(n, 0, -1):
            fact_inv[i-1] = fact_inv[i]*i%self.mod
        return fact_inv
    def comb(self, m, k):
        return self.fact[m]*self.fact_inv[k]*self.fact_inv[m-k]%self.mod

comb = Combination(n, MOD)
comb.comb(5,2) # -> 10