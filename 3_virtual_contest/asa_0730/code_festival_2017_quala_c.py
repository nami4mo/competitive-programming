h,w = map(int, input().split())
alp_d = {chr(ord('a') + i): 0 for i in range(26)}

for _ in range(h):
    s = list(input())
    for si in s:
        alp_d[si] += 1
        alp_d[si] %= 4

r4 = [0]*4
for v in alp_d.values():
    r4[v] += 1

if w%2 == 0 and h%2 == 0:
    if r4[1] == 0 and r4[2] == 0 and r4[3] == 0 and r4[0] > 0:
        print('Yes')
    else:
        print('No')

elif w%2 == 0 and h%2 != 0:
    if r4[1] == 0 and r4[2] <= w//2 and r4[3] == 0:
        print('Yes')
    else:
        print('No')

elif h%2 == 0 and w%2 != 0:
    if r4[1] == 0 and r4[2] <= h//2 and r4[3] == 0:
        print('Yes')
    else:
        print('No')       

else:
    cnt2 = (w-1)//2 + (h-1)//2
    if r4[1] == 1 and r4[2] <= cnt2 and r4[3] == 0:
        print('Yes')
    elif r4[1] == 0 and r4[2] <= cnt2-1 and r4[3] == 1:
        print('Yes')
    else:
        print('No')