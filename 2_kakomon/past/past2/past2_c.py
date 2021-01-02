n = int(input())

sl = []
for _ in range(n):
    row = list(input())
    sl.append(row)

# print(sl)
for i in range(n-2, -1, -1):
    for j in range(1, 2*n-2):
        # print(i,j)
        if sl[i][j] == '#':
            if 'X' in [sl[i+1][j-1], sl[i+1][j], sl[i+1][j+1]]:
                sl[i][j] = 'X'


for row in sl:
    print(''.join(row))