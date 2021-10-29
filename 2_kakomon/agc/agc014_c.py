
from collections import deque
def main():
    h,w,k=map(int, input().split())
    sl=[list(input()) for _ in range(h)]
    sy,sx=-1,-1
    for y in range(h):
        for x in range(w):
            if sl[y][x]=='S':sy,sx=y,x

    q=deque()
    q.append((sy,sx))
    dists=[[-1]*w for _ in range(h)]
    dists[sy][sx]=0
    ans=10**18
    while q:
        y,x=q.popleft()
        cand=min(y,x,h-y-1,w-x-1)
        cand=(cand-1)//k+1
        if cand==0:
            print(1)
            return
        ans=min(ans,cand)
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            yy,xx=y+dy,x+dx
            if not(0<=yy<h and 0<=xx<w):continue
            if sl[yy][xx]=='#':continue
            if dists[yy][xx]!=-1:continue
            if dists[y][x]>=k:continue
            q.append((yy,xx))
            dists[yy][xx]=dists[y][x]+1
    print(ans+1)


if __name__ == "__main__":
    main()