n = int(input())

num_cnt = [ [0]*9  for _ in range(9)]
for i in range(n):
    num = i+1
    num_s = str(num)
    top = int(num_s[0]) -1
    last = int(num_s[-1]) -1
    if top == -1 or last == -1:
        continue
    num_cnt[top][last] += 1

ans = 0
for x in range(0,9):
    for y in range(0,9):
        ans += num_cnt[x][y] * num_cnt[y][x]
print(ans)