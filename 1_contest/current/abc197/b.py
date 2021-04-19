h,w,x,y=map(int, input().split())
x-=1
y-=1
sl=[]
for _ in range(h):
    row=input()
    sl.append(row)

ans=1
for i in range(x-1,-1,-1):
    if sl[i][y]=='.': ans+=1
    else:break
for i in range(x+1,h):
    if sl[i][y]=='.': ans+=1
    else:break

for i in range(y-1,-1,-1):
    if sl[x][i]=='.': ans+=1
    else:break
for i in range(y+1,w):
    if sl[x][i]=='.': ans+=1
    else:break

print(ans)