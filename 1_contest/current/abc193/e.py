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
    x,y,p,q=map(int, input().split())
    a=p+q
    mod=(x+y)*2
    ans=10**20
    for b in range(p,p+q):
        for c in range(x,x+y):
            right=(c-b)%mod
            xx=calc(a,right,mod)
            if xx==-1:continue
            val=a*xx+b
            ans=min(ans,val)
    if ans==10**20:ans='infinity'
    ansl.append(ans)
for a in ansl:print(a)

            


    # looplen=(x+y)**2
    # okrleft=x
    # okright=x+y
    # baby={}
    # lensq=int(looplen**0.5)+1