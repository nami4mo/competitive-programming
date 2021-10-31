from itertools import product

s = input()
n = len(s)
# dsum = 0
# for si in s:
#     dsum += int(si)

ite = list(product(range(2),repeat=n))
ans = n
for pattern in ite:
    cnt = 0
    dsum = 0
    for i, v in enumerate(pattern):
        if v == 0:
            dsum += int(s[i])
        else:
            cnt += 1
    if dsum%3 == 0:
        ans = min(ans,cnt)

if ans == n:
    print(-1)
else:
    print(ans)