from collections import deque

w,h=map(int, input().split())
sl=[]
sl.append([0]*(w+2))
for _ in range(h):
    row=[0]+list(map(int, input().split()))+[0]
    sl.append(row)
sl.append([0]*(w+2))

w+=2
h+=2
nums=[[0]*w for _ in range(h)]
q=deque([(0,0)])
while q:
    y,x=q.popleft()
    for dx in [-1,1]:
        if not 0<=x+dx<w:continue
        if nums[y][x+dx]!=0 or sl[y][x+dx]==1:continue
        nums[y][x+dx]=-1
        q.append((y,x+dx))
    if y%2==0: dxs=[-1,0]
    else: dxs=[0,1]
    for dy in [-1,1]:
        for dx in dxs:
            yy=y+dy
            xx=x+dx
            if not (0<=xx<w and 0<=yy<h):continue
            if nums[yy][xx]!=0 or sl[yy][xx]==1:continue
            nums[yy][xx]=-1
            q.append((yy,xx))
# print(nums)

num=1
for i in range(h):
    for j in range(w):
        if sl[i][j]==0 or nums[i][j]!=0:continue
        q=deque([(i,j)])
        nums[i][j]=num
        while q:
            y,x=q.popleft()
            for dx in [-1,1]:
                xx=x+dx
                if not 0<=xx<w:continue
                # if nums[y][xx]!=0 or sl[y][xx]==0:continue
                if nums[y][xx]!=0:continue
                nums[y][xx]=num
                q.append((y,xx))
            if y%2==0: dxs=[-1,0]
            else: dxs=[0,1]
            for dy in [-1,1]:
                for dx in dxs:
                    yy=y+dy
                    xx=x+dx
                    if not (0<=xx<w and 0<=yy<h):continue
                    # if nums[yy][xx]!=0 or sl[yy][xx]==0:continue
                    if nums[yy][xx]!=0:continue
                    nums[yy][xx]=num
                    q.append((yy,xx))
        num+=1
# print(nums)

ans=0
for y in range(h):
    for x in range(w):
        if nums[y][x]==-1:continue
        num=nums[y][x]
        ans+=6
        for dx in [-1,1]:
            xx=x+dx
            if nums[y][xx]==num:ans-=1
        if y%2==0: dxs=[-1,0]
        else: dxs=[0,1]
        for dy in [-1,1]:
            for dx in dxs:
                yy=y+dy
                xx=x+dx
                if nums[yy][xx]==num:ans-=1
print(ans)