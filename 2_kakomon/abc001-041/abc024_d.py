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
    

a=int(input())
b=int(input())
c=int(input())
MOD=10**9+7
r=(b*c-a*c)*modinv(a*b-b*c+c*a,MOD)
c=(b*c-a*b)*modinv(a*c-b*c+a*b,MOD)
print(r%MOD,c%MOD)