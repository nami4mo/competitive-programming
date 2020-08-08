from fractions import gcd
from math import gcd

def lcm(x,y):
    return (x * y) // gcd(x, y)


def get_2(x):
    curr_2 = 0
    curr_x = x
    while curr_x%2 == 0:
        curr_x = curr_x//2
        curr_2 += 1
    return curr_2

n,m = map(int, input().split())
al = list(map(int, input().split()))


if n == 1:
    cnt = (m-al[0]//2)//al[0] + 1
    print(cnt)
    exit()



a2_set = set()
a2_set.add(get_2(al[0]))
for a in al:
    two_cnt = get_2(a)
    if two_cnt not in a2_set:
        print(0)
        exit()
    a2_set.add(two_cnt)


curr_lcm = 1
for a in al:
    curr_lcm = lcm(curr_lcm, a//2)

lcm_cnt = m//curr_lcm
lcm_cnt = (lcm_cnt+2-1)//2

# print(curr_lcm)
print(lcm_cnt)



