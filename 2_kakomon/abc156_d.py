# PyPy -> OK
# Python -> TLE

def pow_k(x, n):
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2
        x%=MOD
    return K * x

# nCk
K_MAX = 10**7
MOD = 10**9 + 7
fac, finv, inv = [0]*(K_MAX+1), [0]*(K_MAX+1), [0]*(K_MAX+1)
# nCk (k<=10^7, n<=10^9)
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


com_init()
n, a, b = map(int, input().split()) 

all_comb = pow_k(2,n)
a_comb = com(n,a)
b_comb = com(n,b)

ans = all_comb - a_comb - b_comb -1
print(ans%MOD)
