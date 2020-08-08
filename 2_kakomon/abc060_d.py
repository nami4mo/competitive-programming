import copy

N, W = map(int, input().split())
wvl = []
first_w, v = map(int, input().split())
wvl.append((first_w,v))
for _ in range(N-1):
    w,v = map(int, input().split())
    # wvl.append((w-first_w,v))
    wvl.append((w,v))

w_set_res = set()
w_set = set()
w_set_res.add(0)
w_set.add(0)
for i in range(N-1):
    next_w_set = set()
    for w in list(w_set):
        for j in range(0,4):
            new_w = w+j+first_w
            if new_w <= W:
                next_w_set.add(new_w)
                w_set_res.add(new_w)
    w_set = copy.deepcopy(next_w_set)

w_set_res.add(0)
# print(w_set_res)
w_list = list(w_set_res)
w_list.sort()

max_w = min(4*N, W-first_w*N)
dp = [ {0:0} for _ in range(N+1)]
for d in dp:
    for w in w_list:
        d[w] = 0

for i in range(N):
    wi,vi = wvl[i]
    for w in w_list:
        if w-wi in w_set_res:
            dp[i+1][w] = max(dp[i][w-wi] + vi, dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]

# print(dp)
print(max(dp[N].values()))