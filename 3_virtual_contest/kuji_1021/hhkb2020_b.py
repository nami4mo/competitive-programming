h,w = map(int, input().split())
sl = []
for _ in range(h):
    row = list(input())
    sl.append(row)

ans = 0
for i in range(h):
    for j in range(w-1):
        if sl[i][j] == '.' and sl[i][j+1] == '.':
            ans += 1

for j in range(w):
    for i in range(h-1):
        if sl[i][j] == '.' and sl[i+1][j] == '.':
            ans += 1

print(ans)