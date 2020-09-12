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


N_MAX = 10**6
MOD = 10**9 + 7
fac, finv, inv = [0]*N_MAX, [0]*N_MAX, [0]*N_MAX
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



def main():
    x, y = map(int, input().split()) 
    com_init()

    a3 = -x+2*y
    b3 = 2*x-y

    if a3%3 != 0 or b3%3 != 0:
        print(0) 
        return

    a = a3//3
    b = b3//3

    print(com(a+b, min(a,b)))

if __name__ == "__main__":
    main()