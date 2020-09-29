x1,y1,x2,y2 = map(int, input().split())
v12x, v12y = x2-x1, y2-y1
v14x, v14y = v12y*(-1), v12x
x4,y4 = x1+v14x, y1+v14y

x3,y3 = x4+v12x, y4+v12y

print(x3,y3,x4,y4)