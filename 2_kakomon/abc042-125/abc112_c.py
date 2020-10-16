n = int(input())
hxyl = []
for _ in range(n):
    x,y,h = map(int, input().split())
    hxyl.append((h,x,y))

hxyl.sort(reverse=True)

for cx in range(101):
    for cy in range(101):
        h,x,y = hxyl[0]
        dx = abs(x-cx)
        dy = abs(y-cy)
        ch = h+dx+dy
        for h,x,y in hxyl[1:]:
            calc_h = ch - abs(x-cx) - abs(y-cy)
            calc_h = max(calc_h,0)
            if h != calc_h:
                break
        else:
            print(cx,cy,ch)
            exit()

