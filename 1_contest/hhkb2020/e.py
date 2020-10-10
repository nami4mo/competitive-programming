
h,w = map(int, input().split())
s = []
k_cnt =0
for _ in range(h):
    row = input()
    k_cnt += row.count('.')
    s.append(row)

cnts = [ [0]*w for _ in range(h) ]
for i in range(h):
    curr = 0
    for j in range(w):
        c = s[i][j]
        if c == '#': curr = 0
        else:
            curr += 1
            cnts[i][j] += curr
            
    curr = 0
    for j in range(w-1,-1,-1):
        c = s[i][j]
        if c == '#': curr = 0
        else:
            curr += 1
            cnts[i][j] += (curr-1)


for j in range(w):
    curr = 0
    for i in range(h):
        c = s[i][j]
        if c == '#': curr = 0
        else:
            curr += 1
            cnts[i][j] += (curr-1)
            
    curr = 0
    for i in range(h-1,-1,-1):
        c = s[i][j]
        if c == '#': curr = 0
        else:
            curr += 1
            cnts[i][j] += (curr-1)

ans = 0
MOD = 10**9+7
all_num = pow(2,k_cnt,MOD)
# print(all_num)
for i in range(h):
    for j in range(w):
        ans += (all_num-pow(2,k_cnt-cnts[i][j],MOD))
        ans %= MOD

print(ans)