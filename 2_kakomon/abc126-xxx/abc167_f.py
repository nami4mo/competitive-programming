n = int(input())
sl_minus = []
sl_plus = []
left_plus = 0
for _ in range(n):
    s = list(input())
    curr_val = 0
    smin = 0
    for si in s:
        if si == '(': curr_val += 1
        else: curr_val -= 1
        smin = min(smin, curr_val)
    if smin >= 0:
        left_plus += curr_val
    elif curr_val >= 0:
        sl_plus.append(((-1)*smin, curr_val))
    elif curr_val < 0:
        sl_minus.append(((-1)*smin, curr_val))

print(left_plus)
print(sl)

sl_plus.sort()
for smin, v in sl_plis:
    if left_plus < smin:
        print('No')
        exit()
    left_plus += v

for 