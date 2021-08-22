
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

'''
    find minimum x(>=0) 
    [a*x = b (mod m)]
'''
from math import gcd
def calc(a,b,m):
    gcd_am=gcd(a,m)
    if gcd_am!=1:
        if b%gcd_am!=0: return -1 # no answer
        a,b,m = a//gcd_am,b//gcd_am,m//gcd_am
    x=(b*modinv(a,m))%m
    return x
    

ansl=[]
for _ in range(int(input())):
    n,s,k=map(int, input().split())
    ans=calc(k,n-s,n)
    ansl.append(ans)
for a in ansl:print(a)