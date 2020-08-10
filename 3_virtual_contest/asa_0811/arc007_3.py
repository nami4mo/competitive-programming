from itertools import product

cl = list(input())
n = len(cl)

all_cl = []
for i in range(n):
    s = cl[i:n] + cl[0:i]
    all_cl.append(s)



ans = 11
bit = 2
ite = list(product(range(bit),repeat=n))
for pattern in ite:
    used = []
    for i, v in enumerate(pattern):
        if v == 1:
            used.append(all_cl[i])
    if not used: continue
    for i in range(n):
        ok_flag = False
        for u in used:
            if u[i] == 'o':
                ok_flag = True
                break
        if not ok_flag:
            break
    else:
        ans = min(ans, len(used))

print(ans)
