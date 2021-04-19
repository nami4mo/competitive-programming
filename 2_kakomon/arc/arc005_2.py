def dd(w):
    dx,dy=0,0
    if 'R' in w:dx=1
    if 'L' in w:dx=-1
    if 'U' in w:dy=-1
    if 'D' in w:dy=1
    return dx,dy


x,y,w=map(str, input().split())
x,y=int(x),int(y)
x-=1
y-=1
cl=[]
for _ in range(9):
    cl.append(list(input()))
dx,dy=dd(w)

ans=[cl[y][x]]
for _ in range(3):
    ny,nx=y+dy,x+dx
    if ny<0:dy=1
    if ny>=9:dy=-1
    if nx<0:dx=1
    if nx>=9:dx=-1
    y,x=y+dy,x+dx
    ans.append(cl[y][x])
    # print(y,x)
print(''.join(ans))