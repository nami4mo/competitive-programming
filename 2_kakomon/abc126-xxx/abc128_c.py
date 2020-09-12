from itertools import product

n,m = map(int, input().split())
ks = []
for _ in range(m):
    sl = list(map(int, input().split()))
    ks.append(sl[1:])

pl = list(map(int, input().split()))


ans = 0
pattern = 2
ite = product(range(pattern),repeat=n)
for it in ite:
    s_on_off = list(it)
    for bulb, p in zip(ks, pl):
        curr_cnt = 0
        for s in bulb:
            if s_on_off[s-1] == 1: curr_cnt+=1
        if curr_cnt%2 != p:
            break
    else:
        ans += 1

print(ans)