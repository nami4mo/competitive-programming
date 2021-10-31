from itertools import product
import copy

h,w,k = map(int, input().split())
cl = []
b_cnt = 0
for _ in range(h):
    row = list(input())
    cl.append(row)
    b_cnt += row.count('#')

# print(b_cnt)

pattern = 2
# ite_h = product(range(pattern),repeat=h)
# ite_w = product(range(pattern),repeat=w)
ite = product(range(pattern),repeat=h+w)
ans = 0

for it in ite:
    curr_it = list(it)
    it_h = curr_it[:h]
    it_w = curr_it[h:]

# for it_h in ite_h:
#     for it_w in ite_w:
    curr_cl = copy.deepcopy(cl)
    cnt = 0
    for hi in range(h):
        if it_h[hi] == 0: continue
        for wi in range(w):
            if curr_cl[hi][wi] == '#':
                curr_cl[hi][wi] = 'r'
                cnt += 1
    for wi in range(w):
        if it_w[wi] == 0: continue
        for hi in range(h):
            if curr_cl[hi][wi] == '#':
                curr_cl[hi][wi] = 'r'
                cnt += 1

    if b_cnt-cnt == k:
        ans += 1
    # print()
    # print(it_h, it_w)
    # print(curr_cl)
    # print(cnt)

print(ans)