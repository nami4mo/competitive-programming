import math

n,m = map(int, input().split())
s = input()
t = input()

if n == m:
    if s == t:
        print(n)
    else:
        print(-1)
    exit()

if m == 1:
    n,m = m,n
    s,t = t,s

if n == 1:
    if s[0] == t[0]:
        print(m)
    else:
        print(-1)
    exit()

lcm = n * m // math.gcd(n, m)

n1 = lcm//n
m1 = lcm//m

lcm2 = n1 * m1 // math.gcd(n1, m1)
stepn = lcm2//n1
stepm = lcm2//m1

for i in range(0,10**5):
    if stepn*i > n-1 or stepm*i > m-1:
        print(lcm)
        break
    if s[stepn*i] != t[stepm*i]:
        print(-1)
        exit()