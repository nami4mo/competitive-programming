from collections import deque
def check_connect(val):
    pl=[[False]*4 for _ in range(4)]
    start=(-1,-1)
    cnt=0
    for y in range(4):
        for x in range(4):
            v=y*4+x
            if val&(1<<v):
                pl[y][x]=True
                start=(y,x)
                cnt+=1
    sz=0
    q=deque()
    q.append(start)
    vis=[[False]*4 for _ in range(4)]
    vis[start[0]][start[1]]=True
    dyx=[(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        y,x=q.popleft()
        sz+=1
        for dy,dx in dyx:
            yy=y+dy
            xx=x+dx
            if not(0<=yy<4 and 0<=xx<4):continue
            if vis[yy][xx]:continue
            if not pl[yy][xx]:continue
            vis[yy][xx]=True
            q.append((yy,xx))
    # print(cnt,sz)
    if sz!=cnt:
        return False
    else:
        for y in range(4):
            for x in range(4):
                if y!=0 and x!=3:
                    if pl[y][x] and (not pl[y-1][x]) and (not pl[y][x+1]) and pl[y-1][x+1]:return False
                if y!=3 and x!=3:
                    if pl[y][x] and (not pl[y+1][x]) and (not pl[y][x+1]) and pl[y+1][x+1]:return False
        
                if pl[y][x]:continue
                q=deque()
                q.append((y,x))
                vis=[[False]*4 for _ in range(4)]
                vis[y][x]=True
                okok=False
                while q:
                    cy,cx=q.popleft()
                    if cy==0 or cy==3 or cx==0 or cx==3:
                        okok=True
                        break
                    for dy,dx in dyx:
                        yy=cy+dy
                        xx=cx+dx
                        if not(0<=yy<4 and 0<=xx<4):continue
                        if vis[yy][xx]:continue
                        if pl[yy][xx]:continue
                        vis[yy][xx]=True
                        q.append((yy,xx))
                if not okok:return False
                
    # print(cnt,sz)


        return True
                

def dbg(val):
    pl=[[0]*4 for _ in range(4)]
    for y in range(4):
        for x in range(4):
            v=y*4+x
            if val&(1<<v):
                pl[y][x]=1
    print('---')
    for row in pl:
        print(*row)

def main():
    al=[list(map(int, input().split())) for _ in range(4)]
    # print(check_connect(17))
    # print(check_connect(33))

    ans=0
    for i in range(1<<16):
        ok=True
        for y in range(4):
            for x in range(4):
                v=y*4+x
                if al[y][x]==1 and i&(1<<v)==0:ok=False
        if ok:
            if check_connect(i):
                ans+=1
                # dbg(i)
                # print(i)
    print(ans)


if __name__ == "__main__":
    main()