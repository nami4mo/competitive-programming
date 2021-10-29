def solve(v):
    cnt=0
    for i in range(1,int(v**0.5)+1):
        if v%i==0:
            cnt+=2
        if i*i==v:
            cnt-=1
    return cnt

x,y=map(int, input().split())
cx,cy=solve(x),solve(y)
if cx>cy:print('X')
elif cx<cy:print('Y')
else:print('Z')