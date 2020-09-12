from math import gcd

n,k = map(int, input().split())
al = list(map(int, input().split()))
a_gcd = al[0]
for a in al[1:]:
    a_gcd = gcd(a_gcd,a)

if k%a_gcd == 0 and k <= max(al):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')