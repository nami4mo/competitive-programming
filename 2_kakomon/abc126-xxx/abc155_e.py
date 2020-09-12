ns = input()
nl = []
for ni in ns[::-1]:
    nl.append(ni)


ans = 0
prev_up = False
for i,ni in enumerate(nl):
    ni = int(ni)
    if prev_up:
        ni += 1
    if ni <= 5:
        ans += ni
        prev_up = False
    else:
        if i == len(nl)-1:
            ans += (1+10-ni)
        else:
            ans += (10-ni)
        prev_up = True

print(ans)