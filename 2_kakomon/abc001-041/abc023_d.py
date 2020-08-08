n = int(input())

hs_list = []
for i in range(n):
    hs_list.append(list(map(int,input().split())))


# ans = 0
left = 0
right = 2*(10**16)
while True:
# for x in range(200000):
    mid = left + (right-left)//2
    t_lim_list = []
    for hs in hs_list:
        t_lim = (mid-hs[0])//hs[1]
        t_lim_list.append(t_lim)
    t_lim_list.sort()

    res = True
    for i, t_lim in enumerate(t_lim_list):
        if i > t_lim:
            res = False
            break

    if res:
        right = mid
    else:
        left = mid
    if right - left <= 1:
        break

    # print(left, right)

    # if res == True:
    #     ans = x
    #     break
print(right)