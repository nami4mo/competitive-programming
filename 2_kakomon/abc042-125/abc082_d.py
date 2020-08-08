import copy

s = input()
target_x, target_y = map(int, input().split())

fl = s.split('T')
f_cnts = [ len(v) for v in fl ]

target_x -= f_cnts[0]
f_cnts = f_cnts[1:]

last_xs = set()
last_ys = set()
last_xs.add(0)
last_ys.add(0)
for i, f_cnt in enumerate(f_cnts):
    if i%2 == 0:
        next_y = f_cnts[i]
        next_last_ys = set()
        for y in list(last_ys):
            next_last_ys.add(y+next_y)
            next_last_ys.add(abs(y-next_y))
        last_ys = copy.deepcopy(next_last_ys)
    else:
        next_x = f_cnts[i]
        next_last_xs = set()
        for x in list(last_xs):
            next_last_xs.add(x+next_x)
            next_last_xs.add(abs(x-next_x))
        last_xs = copy.deepcopy(next_last_xs)


if (target_x in last_xs or -1*target_x in last_xs) and (target_y in last_ys or -1*target_y in last_ys):
    print('Yes')
else:
    print('No')
