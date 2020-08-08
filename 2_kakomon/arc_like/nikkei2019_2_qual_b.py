n = int(input())
dl = list(map(int, input().split()))

MOD = 998244353
ans = 0
d_comb = [0]*n

if dl[0] == 0:
    ans = 1
    d_comb[0] = 1
else:
    print(0)
    exit()

dl.sort()
if n == 1:
    print(1)
    exit()
elif dl[1] == 0:
    print(0)
    exit()

for d in dl[1:]:
    ans *= d_comb[d-1]
    d_comb[d] += 1
    ans %= MOD

print(ans)    
