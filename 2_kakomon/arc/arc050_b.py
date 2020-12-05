r,b=map(int, input().split())
x,y=map(int, input().split())

ok, ng = -1, 10**19+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    ok_flag = False
    # ...

    red = r-mid
    blue = b-mid

    red_rem = red//(x-1)
    blue_rem = blue//(y-1)

    if red >= 0 and blue >= 0 and red_rem + blue_rem >= mid:
        ok_flag = True

    if ok_flag:
        ok = mid
    else:
    	ng = mid
print(ok)
