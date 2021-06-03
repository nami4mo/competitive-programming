INF=10**18
def mul(a,b):
    if a>INF//b:return -1
    else:return a*b

from math import gcd
a,b=map(int, input().split())
g=gcd(a,b)
lcm=mul(g,mul(a//g,b//g))
if lcm<0:print('Large')
else:print(lcm)
