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


n,k = map(int, input().split())
r = n-k
com_init()

for i in range(1,k+1):
    ans = 0
    bi = com(k+i-1 -i, i-1)
    if i == 1:
        if r == 0: ri_m1 = 1
        else: ri_m1 = 0
    else:
        ri_m1 = com(r+i-2 -(i-1), i-2)
    ri = com(r+i-1 -i, i-1) if r >= i else 0
    ri_p1 = com(r+i -(i+1), i) if r >= i+1 else 0
    ans += bi*ri_m1
    ans += bi*ri*2
    ans += bi*ri_p1
    ans%=MOD
    print(ans)