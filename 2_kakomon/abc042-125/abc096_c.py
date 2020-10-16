h,w = map(int, input().split())
sl = []
sl.append('.'*(w+2))
for _ in range(h):
    row = '.'+input()+'.'
    sl.append(row)
sl.append('.'*(w+2))

for i in range(h+2):
    for j in range(w+2):
        if sl[i][j] == '#':
            if sl[i-1][j] == '.' and sl[i+1][j] == '.' and sl[i][j-1] == '.' and sl[i][j+1] == '.':
                print('No')
                exit()

print('Yes')
