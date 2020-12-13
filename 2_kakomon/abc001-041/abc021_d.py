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

n=int(input())
k=int(input())

MOD=10**9+7
top=1
bottom=1
for i in range(k):
    top*=(n+k-1-i)
    bottom*=(i+1)
    top%=MOD
    bottom%=MOD
ans = top*modinv(bottom,MOD)
print(ans%MOD)