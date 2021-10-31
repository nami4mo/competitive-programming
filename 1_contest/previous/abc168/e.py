import math
MOD =1000000007


def pow_k(x, n):
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2
        # print(K,x)
        x%=MOD
    return K * x


n = int(input())

a_b_d = {}

a_zero_cnt = 0
b_zero_cnt = 0
ab_zero_cnt = 0

for i in range(n):
    a, b = map(int, input().split()) 
    if a==0 and b!=0:
        a_zero_cnt += 1
    elif  a!=0 and b==0:
        b_zero_cnt += 1
    elif a == 0 and b == 0:
        ab_zero_cnt += 1
    else:
        gcd_ab = math.gcd(a,b)
        a = a//gcd_ab
        b = b//gcd_ab
        if a > 0 and b < 0:
            a *= -1
            b *= -1
        elif a < 0 and b < 0:
            a *= -1
            b *=-1
        a_b_d.setdefault((a,b),0)
        a_b_d[(a,b)] += 1


done_list = set()
pair_cnt = []
uniq_cnt = 0
for k,v in a_b_d.items():
    comp_pair1 = (-k[1], k[0])
    comp_pair2 = (k[1], -k[0])
    if k in done_list:
        continue
    if comp_pair1 in a_b_d:
        done_list.add(comp_pair1)
        pair_cnt.append((v,a_b_d[comp_pair1]))
    elif comp_pair2 in a_b_d:
        done_list.add(comp_pair2)
        pair_cnt.append((v,a_b_d[comp_pair2]))
    else:
        uniq_cnt += v

# print(a_b_d)

ans = pow_k(2,uniq_cnt) % MOD
for pair in pair_cnt:
    ans *= (pow_k(2,pair[0]) + pow_k(2,pair[1]) -1 )
    ans%=MOD

zero_m = max(pow_k(2,a_zero_cnt) + pow_k(2,b_zero_cnt) -1, 1)
ans *= zero_m
ans += ab_zero_cnt
ans -= 1
print(ans%MOD)