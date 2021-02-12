sx,sy,gx,gy = map(int, input().split())
x = (sx*gy+gx*sy)/(sy+gy)
print(x)