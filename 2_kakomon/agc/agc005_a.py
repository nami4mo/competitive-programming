s = input()
prev_s_cnt = 0
del_cnt = 0
for si in s:
    if si == 'S':
        prev_s_cnt += 1
    else:
        if prev_s_cnt == 0:
            pass
        else:
            prev_s_cnt -= 1
            del_cnt += 2

print(len(s)-del_cnt)