x,y = map(int, input().split())
if 0 <= x and x <= y:
    print(y-x)
elif 0 <= y and y <= x:
    ans1 = 1+(x-y)+1
    ans2 = 1+(y+x)
    print(min(ans1,ans2))
elif x <= 0 and 0 <= y:
    ans1 = y-x
    if abs(x) >= y:
        ans2 = abs(x)-y+1
    else:
        ans2 = 1+(y-abs(x))
    print(min(ans1,ans2))

elif y <= 0 and 0 <= x:
    if abs(y) >= x:
        print(abs(y)-x+1)
    else:
        print(1+x-abs(y))

elif x <= 0 and y <= 0 and x <= y:
    print(y-x)
else:
    print(1+x-y+1)