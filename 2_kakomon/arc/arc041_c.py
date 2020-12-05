n,l = map(int, input().split())

xdl = []
for _ in range(n):
    x,d = map(str, input().split())
    x = int(x)
    xdl.append((x,d))

ans = 0
i = 0
if xdl[0][1] == 'L':
    cnt = 0
    while True:
        if i >= n or xdl[i][1] == 'R': break
        ans += (xdl[i][0]-1)
        cnt += 1
        i += 1
    ans -= cnt*(cnt-1)//2


while True:
    right_inds = []
    while True:
        if i >= n or xdl[i][1] == 'L': break
        right_inds.append(xdl[i][0])
        i+=1
    # space = xdl[i][0]-1 if i < n else l
    if not right_inds: break
    right_val = 0
    for rv in right_inds:
        right_val += (right_inds[-1]-rv)
    rlen = len(right_inds)
    right_val -= rlen*(rlen-1)//2

    if i >= n:
        ans += right_val
        ans += rlen*(l-right_inds[-1])
        break

    left_top = xdl[i][0]
    # left_space = right_inds[-1]+1
    l_cnt = 0
    left_val = 0
    while True:
        if i >= n or xdl[i][1] == 'R': break
        left_val += (xdl[i][0]-left_top)
        l_cnt+=1
        i+=1
    left_val -= l_cnt*(l_cnt-1)//2

    ans += right_val
    ans += left_val
    ans += max(rlen,l_cnt)*(left_top-right_inds[-1]-1)

    # print(right_val)
    # print(left_val)

    if i >= n:
        break

print(ans)