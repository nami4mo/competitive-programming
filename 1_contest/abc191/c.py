h,w=map(int, input().split())
sl=[]
for _ in range(h):
    row=list(input())
    sl.append(row)

ans=0
for y in range(h-1):
    for x in range(w-1):
        cnt=0
        if sl[y][x]=='#':cnt+=1
        if sl[y+1][x]=='#':cnt+=1
        if sl[y][x+1]=='#':cnt+=1
        if sl[y+1][x+1]=='#':cnt+=1
        if cnt==1 or cnt==3:
            ans+=1

print(ans)