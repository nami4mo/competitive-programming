d = int(input())
cl = list(map(int, input().split()))
sl = []
for _ in range(d):
    sl.append(list(map(int, input().split())))

tl = []
# for _ in range(d):
#     tl.append(int(input()))

last_di = [-1]*26
ans = 0
for day in range(d):
    best_t = 0
    best_t_val = -999999999999
    for t in range(26):
        curr_val = sl[day][t]*2
        for i in range(26):
            if i == t: continue
            curr_val -= (day-last_di[i])*cl[i]*3
        if curr_val >= best_t_val:
            best_t = t
            best_t_val = curr_val
    tl.append(best_t+1)
    last_di[best_t] = day
    ans += best_t_val
    # print(ans)
    # print('-- {}---'.format(day))
    # print(best_t)
    # print(last_di)

for t in tl:
    print(t)

# for day, t in enumerate(tl):
#     ans += sl[day][t-1]
#     last_di[t-1] = day
#     for ld, c in zip(last_di, cl):
#         # if ld == -1: continue
#         ans -= (day-ld)*c
#     print(ans)