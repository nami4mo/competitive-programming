n,m,sx,sy = map(int, input().split())
for y in range(sy,m+1):
    print(sx,y)

for y in range(sy-1,0,-1):
    print(sx,y)

to_back = True
for x in range(1,n+1):
    if x == sx: continue
    if to_back:
        for y in range(1,m+1):
            print(x,y) 
    else:
        for y in range(m,0,-1):
            print(x,y)
    to_back = not to_back

    