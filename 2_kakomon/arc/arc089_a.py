n = int(input())
px,py = 0,0
pt = 0
for _ in range(n):
    t,x,y = map(int, input().split())
    dt = t-pt
    d = abs(px-x) + abs(py-y)
    if d > dt or (d-dt)%2 == 1:
        print('No')
        exit()
    px,py = x,y
    pt = t
print('Yes')