def dfs(sl,y,x,prevs,h,w,cnt):
    # print('--',y,x)
    dxy=[[-1,0],[1,0],[0,-1],[0,1]]
    used=[]
    if len(prevs)==cnt:
        # print(prevs)
        print(cnt)
        cy,cx=y,x
        while True:
            print(cy+1,cx+1)
            cy,cx=prevs[(cy,cx)]
            if cy==-1:exit()

    for dx,dy in dxy:
        yy=y+dy
        xx=x+dx
        if yy<0 or h<=yy or xx<0 or w<=xx:continue
        if sl[yy][xx]=='.':continue
        if (yy,xx) in prevs: continue
        used.append((yy,xx))
        prevs[(yy,xx)]=(y,x)
        dfs(sl,yy,xx,prevs,h,w,cnt)
        prevs.pop((yy,xx))
    # print('----',y,x)

    # for yy,xx in used:
    #     print('pop',yy,xx)
    #     prevs.pop((yy,xx))
        

h,w=map(int, input().split())
sl=[]
cnt=0
for _ in range(h):
    row=list(input())
    sl.append(row)
    cnt+=row.count('#')

for i in range(h):
    for j in range(w):
        if sl[i][j]=='.':continue
        prevs={(i,j):(-1,-1)}
        dfs(sl,i,j,prevs,h,w,cnt)