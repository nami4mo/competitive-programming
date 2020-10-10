h,w = map(int, input().split())
s = []
for _ in range(h):
    row = input()
    s.append(row)

ans = 0
for i in range(h):
    row = s[i]
    for j1,j2 in zip(row[:-1],row[1:]):
        if j1 == '.' and j2 == '.': ans += 1

for i in range(w):
    for j in range(h-1):
        if s[j][i] == '.' and s[j+1][i] == '.': ans += 1

print(ans)