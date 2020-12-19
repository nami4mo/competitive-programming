from math import gcd, ceil
def ext_gcd(a, b, x, y):
    if b == 0:
        x[0] = 1
        y[0] = 0
        return a
    d = ext_gcd(b, a%b, y, x)
    y[0] -= a//b * x[0]
    return d


def solve2(n,s,k):
    k%=n
    g=gcd(k,n)

    if s%g!=0:
        return -1

    n//=g
    s//=g
    k//=g

    a=(-1)*k
    b=n
    x,y = [0],[0]
    ext_gcd(a,b,x,y)
    x,y = x[0],y[0]
    x*=s
    y*=s
    mmin = ceil((-x+1)/n)
    # mmin = -x//n +1
    a = n*mmin+x
    # while a<0:
    #     a+=n
    return a

    # ok, ng = 10**18, (-1)*10**18
    # while abs(ok-ng) > 1:
    #     mid = (ok+ng)//2
    #     if n*mid+x>0:
    #         ok = mid
    #     else:
    #         ng = mid
    # return n*ok+x


t=int(input())
ansl=[]
for _ in range(t):
    n,s,k=map(int, input().split())
    ans = solve2(n,s,k)
    ansl.append(ans)

for a in ansl:print(a)