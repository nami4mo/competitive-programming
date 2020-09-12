from math import gcd
def lcm(x,y): return (x * y) // gcd(x, y)

n = int(input())
nicos = [25,2525,252525,25252525]

# nico_set = set()
ans = 0



# for i in range(1,n//25+1):
#     for nico in nicos:
#         if i%nico:
#             ans +=


for i in range(1,10**8):
    v = 25*i
    if v > n:
        break
    # if not v in nico_set:
    ans += 1

print(ans)