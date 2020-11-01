for _ in range(int(input())):
    x,y = map(int, input().split())
    c = list(map(int, input().split()))
    c11 = min(c[0],c[1]+c[5])
    c_1_1 = min(c[3],c[2]+c[4])
    c01 = min(c[1],c[0]+c[2])
    c10 = min(c[5],c[0]+c[4])
    c0_1 = min(c[4],c[3]+c[5])
    c_10 = min(c[2],c[3]+c[1])

    if x >= 0 and y >= 0:
        m = min(x,y)
        ans = c11*m
        x-=m
        y-=m
        ans += c10*x
        ans += c01*y
    elif x >= 0 and y < 0:
        ans = c10*x + c0_1*abs(y)
    elif x < 0 and y >= 0:
        ans = c_10*abs(x) + c01*y
    else:
        x = abs(x)
        y = abs(y)
        m = min(x,y)
        ans = c_1_1*m
        ans += c_10*(x-m)
        ans += c0_1*(y-m)
    print(ans)
