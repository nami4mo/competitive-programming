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


n,a,b = map(int, input().split())
MOD = 10**9+7
ncnt = pow(2,n,MOD)-1
acnt = 1
for i in range(a):
    acnt *= (n-i)
    acnt *= modinv(i+1,MOD)
    acnt %= MOD

bcnt = 1
for i in range(b):
    bcnt *= (n-i)
    bcnt *= modinv(i+1,MOD)
    bcnt %= MOD

ans = ncnt - acnt - bcnt
print(ans%MOD)
