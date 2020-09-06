n,k,c = map(int, input().split())
s = input()
sr = s[::-1]
lcnt = [0]*n
rcnt = [0]*n

last_i = -10**8
cnt = 0
for i in range(n):
    if s[i] == 'o' and i - last_i > c:
        cnt += 1
        last_i = i
    lcnt[i] = cnt


last_i = -10**8
cnt = 0
for i in range(n):
    if sr[i] == 'o' and i - last_i > c:
        cnt += 1
        last_i = i
    rcnt[i] = cnt
rcnt = rcnt[::-1]


for i in range(n):
    if s[i] == 'x': continue
    if i > 0: l = lcnt[i-1]
    else: l = 0
    if i < n-1: r = rcnt[i+1]
    else: r = 0
    if l+r < k:
        print(i+1)
