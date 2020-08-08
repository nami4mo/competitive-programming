# nCk ( O(N) )
N_MAX = 100
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


n,p = map(int, input().split())
al = list(map(int, input().split()))
zero = 0
one = 0
com_init()
for a in al:
    if a%2 == 0: zero+=1
    else: one+=1


zero_comb = pow(2,zero)
one_comb = 0
if p == 0:
    for i in range(0,one+1,2):
        one_comb += com(one,i)
else:
    for i in range(1,one+1,2):
        one_comb += com(one,i)

print(zero_comb*one_comb)