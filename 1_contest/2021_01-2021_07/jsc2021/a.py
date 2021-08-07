x,y,z=map(int, input().split())
v=y/x
for i in range(1000000,-1,-1):
    vv=i/z
    if v>vv:
        print(i)
        exit()