h,w=map(int, input().split())
dl=[list(input()) for _ in range(h)]

D=[(-1,0),(1,0),(0,-1),(0,1)]
for y in range(h):
    for x in range(w):
        if dl[y][x]!='.':continue
        ok=[True]*6
        for (dy,dx) in D:
            yy=y+dy
            xx=x+dx
            if 0<=yy<h and 0<=xx<w and dl[yy][xx]!='.':
                ok[int(dl[yy][xx])]=False
        for i in range(1,6):
            if ok[i]:
                dl[y][x]=i
                break

# print(dl)

for row in dl:
    row=map(str,row)
    print(''.join(row))