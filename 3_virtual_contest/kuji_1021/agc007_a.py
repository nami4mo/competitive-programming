h,w = map(int, input().split())
sl = []
cnt = 0
for _ in range(h):
    row = list(input())
    sl.append(row)
    cnt += row.count('#')

if cnt != h+w-1:
    print('Impossible')
    exit()

y,x = 0,0
for i in range(h+w-2):
    if y < h-1 and sl[y+1][x] == '#':
        y+=1
    elif x < w-1 and sl[y][x+1] == '#':
        x+=1
    else:
        print('Impossible')
        exit()

if y == h-1 and x == w-1:
    print('Possible')
else:
    print('Impossible')
