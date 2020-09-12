from bisect import bisect_left, bisect_right

s = input()
t = input()

alp_d = {chr(ord('a') + i): [] for i in range(26)}
for i,si in enumerate(s):
    alp_d[si].append(i)

# print(alp_d)

curr_i = -1
loop = 0
for ti in t:
    # print('---',ti)
    if not alp_d[ti]:
        print(-1)
        exit()
    # bより大きい最小要素のindex/value
    ind = bisect_right(alp_d[ti], curr_i)
    ind = ind if 0 <= ind < len(alp_d[ti]) else None
    detected_i = alp_d[ti][ind] if ind is not None else None
    # print(ind)
    if detected_i is not None:
        curr_i = detected_i
    else:
        loop += 1
        curr_i = min(alp_d[ti])

ans = loop*(len(s)) + curr_i+1
print(ans)