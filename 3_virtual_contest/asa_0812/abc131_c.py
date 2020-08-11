from math import gcd

def lcm(x,y):
    return (x * y) // gcd(x, y)

a,b,c,d = map(int, input().split())

a_cnt = 0
a_cnt = (b//c) - ((a-1)//c)
b_cnt = (b//d) - ((a-1)//d)

lcmab = lcm(c,d)
ab_cnt = (b//lcmab) - ((a-1)//lcmab)

ans = (b-a+1) - a_cnt -b_cnt + ab_cnt
print(ans)