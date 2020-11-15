h,w = map(int, input().split())
sl = []
for _ in range(h):
    row = list(input())
    sl.append(row)

cums_h = [0]*h
cums_w = [0]*w
cums_naname = {}
for i in range( -(w-1), (h-1)+1):
    cums_naname[i] = 0

dp = [ [0]*(w) for _ in range(h)]
dp[0][0] = 1
cums_h[0] = 0
cums_w[0] = 0
cums_naname[0] = 0

MOD = 10**9+7

for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            cums_h[0] = 1
            cums_w[0] = 1
            cums_naname[0] = 1
        elif sl[i][j] == '#':
            cums_h[i] = 0
            cums_w[j] = 0
            cums_naname[i-j] = 0
        else:
            v = cums_h[i]+cums_w[j]+cums_naname[i-j]
            v %= MOD
            dp[i][j] = v
            cums_h[i] += v
            cums_w[j] += v
            cums_naname[i-j] += v
        # print(cums_h)
# 
# print(cums_h)
print(dp[-1][-1])