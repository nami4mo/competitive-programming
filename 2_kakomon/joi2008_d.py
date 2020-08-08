# n, m = map(int, input().split()) 
# a_list = []

m = int(input())

sx, sy = map(int, input().split()) 
seiza_list = []
for i in range(m-1):
    x, y = map(int, input().split()) 
    dx, dy = x-sx, y-sy
    seiza_list.append([dx,dy])

n = int(input())
pic_list = []
for i in range(n):
    x, y = map(int, input().split()) 
    pic_list.append([x,y])
# pic_set = set(pic_list)


for pic_xy in pic_list:
    for seiza_xy in seiza_list:
        flag = True
        x = pic_xy[0] + seiza_xy[0]
        y = pic_xy[1] + seiza_xy[1]
        if not [x,y] in pic_list:
            flag = False
            break
    if flag:
        print(pic_xy[0] - sx, pic_xy[1]-sy)