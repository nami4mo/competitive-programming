n = int(input())
slp = []
slm = []
for _ in range(n):
    s = input()
    max_r = 0
    curr_lr = 0
    for si in s:
        if si=='(': curr_lr+=1
        else: curr_lr-=1
        max_r = max(max_r, (-1)*curr_lr)

    max_l = 0
    curr_lr = 0
    for si in s[::-1]:
        if si=='(': curr_lr+=1
        else: curr_lr-=1
        max_l = max(max_l, curr_lr)

    if curr_lr >= 0:
        slp.append((max_l,max_r,curr_lr))
    else:
        slm.append((max_l,max_r,curr_lr))

slp.sort(key=lambda x: x[1])
slm.sort(key=lambda x: -x[0])
# slp.sort(key=lambda x: (x[0],-x[1]))
# slm.sort(key=lambda x: x[0]-x[1])

curr_l = 0
for max_l, max_r, lp in slp+slm:
    if curr_l < max_r:
        print('No')
        exit()
    else:
        curr_l+=lp

if curr_l == 0:
    print('Yes')
else:
    print('No')