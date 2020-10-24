c = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    v = c[i][0]
    for j in range(3):
        c[i][j] -= v

if c[0] != c[1] or c[1] != c[2] or c[2] != c[0]:
    print('No')
else:
    print('Yes')