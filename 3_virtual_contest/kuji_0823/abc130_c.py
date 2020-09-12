w,h,x,y = map(int, input().split())
a = w*h/2
if 2*x == w and 2*y == h:
    print(a, 1)
else:
    print(a,0)