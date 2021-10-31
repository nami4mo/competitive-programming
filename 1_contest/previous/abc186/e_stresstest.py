from math import gcd, ceil
from random import randint, shuffle, sample, choice, seed
import time

def ext_gcd(a, b, x, y):
    if b == 0:
        x[0] = 1
        y[0] = 0
        return a
    d = ext_gcd(b, a%b, y, x)
    y[0] -= a//b * x[0]
    return d


def solve1(n,s,k):
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
    mmin = ceil(-x/n)
    a = n*mmin+x
    while a<0:
        a+=n
    lastb = (g*s)+(g*k)*a
    if lastb%(n*g)==0:
        return a
    else:
        return -1


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
    mmin = ceil(-x/n)
    a = n*mmin+x
    if a<=0:
        print(n,s,k)
        print(-x)
        print(a)
    # if a < 0:
    #     print(a)
    lastb = (g*s)+(g*k)*a
    if lastb%(n*g)==0:
        return a
    else:
        return -1


if __name__ == "__main__":
    loop=10**5
    seed(time.time())
    NMAX=10**9
    # NMAX=10**2
    for i in range(loop):
        n = randint(2,NMAX)
        s = randint(1,n-1)
        k = randint(1,NMAX)
        # k = n
        # k = n
        ans1 = solve1(n,s,k)
        ans2 = solve2(n,s,k)
        if ans1!=ans2:
        # if ans2 < -1:
            print('-----')
            print(n,s,k)
            print('ans1: ',ans1)
            print('ans2: ',ans2)
