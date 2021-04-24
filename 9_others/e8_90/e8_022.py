from math import gcd
a,b,c=map(int, input().split())
g=gcd(a,b)
g=gcd(g,c)
ans=a//g+b//g+c//g-3
print(ans)