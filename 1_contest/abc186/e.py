from math import gcd, ceil
def ext_gcd(a, b, x, y):
    if b == 0:
        x[0] = 1
        y[0] = 0
        return a
    d = ext_gcd(b, a%b, y, x)
    y[0] -= a//b * x[0]
    return d


t=int(input())
ansl=[]
for _ in range(t):
    n,s,k=map(int, input().split())
    k%=n
    g=gcd(k,n)

    if s%g!=0:
        ansl.append(-1)
        continue

    n//=g
    s//=g
    k//=g

    a=(-1)*k
    b=n
    x,y = [0],[0]
    ext_gcd(a,b,x,y)
    x,y = x[0],y[0]
    x*=(s)
    y*=(s)
    kmin = ceil((-1)*x/n)
    a = n*kmin+x
    # while a<0:
    #     a+=n
    lastb = (g*s)+(g*k)*a
    if lastb%(n*g)==0:
        ansl.append(a)
    else:
        ansl.append(-1)

for a in ansl:print(a)