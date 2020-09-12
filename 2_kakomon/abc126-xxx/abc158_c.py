a, b =map(int, input().split())

for x in range(0,10**6):
    # print('---')
    # print(x)
    ax = (8*x)//100
    bx = (10*x)//100
    # print(ax,bx)
    if ax == a and bx == b:
        print(x)
        break
else:
    print(-1)