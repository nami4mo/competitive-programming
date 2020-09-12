h,w,d = map(int, input().split())

al = [list(map(int, input().split())) for _ in range(h)]
v_to_xy = [(-1,-1)]*(h*w+1)
v_to_xy[0] = v_to_xy[d]
for i in range(h):
    for j in range(w):
        v_to_xy[al[i][j]] = (i,j)

dd = []
for i in range(d):
    csum = 0
    cumsum = []
    prev = v_to_xy[i]
    for j in range(i,h*w+1,d):
        if j == 0:
            cumsum.append(0)
            continue
        x,y = v_to_xy[j]
        diff = abs(prev[0]-x) + abs(prev[1]-y)
        csum += diff
        cumsum.append(csum)
        prev = (x,y)
    dd.append(cumsum)
    
# print(dd)

ansl = []
for _ in range(int(input())):
    l,r = map(int, input().split())
    drem = r%d
    ri = (r-drem)//d
    li = (l-drem)//d
    # print(drem,li,ri)
    ans = dd[drem][ri] - dd[drem][li]
    ansl.append(ans)

for ans in ansl: print(ans)