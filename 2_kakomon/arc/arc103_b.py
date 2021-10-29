MAX=32
def solve(x,y):
    u=x+y
    v=x-y
    cu=0
    cv=0
    res=[]
    for i in range(MAX,-1,-1):
        d=(1<<i)
        if cu<u and cv<v:
            cu+=d
            cv+=d
            res.append('R')
        elif cu<u and cv>v:
            cu+=d
            cv-=d
            res.append('U')
        elif cu>u and cv<v:
            cu-=d
            cv+=d
            res.append('D')
        else:
            cu-=d
            cv-=d
            res.append('L')
    return res

n=int(input())
xyl=[]
for _ in range(n):
    x,y=map(int, input().split())
    xyl.append((x,y))
for x,y in xyl:
    if (xyl[0][0]+xyl[0][1])%2!=(x+y)%2:
        print(-1)
        exit()


dl=[1<<i for i in range(MAX,-1,-1)]
if (xyl[0][0]+xyl[0][1])%2==0:
    dl.append(1)
print(len(dl))
print(*dl)
    

def check(c):
    x,y=0,0
    for i,d in enumerate(dl):
        if c[i]=='L':x-=d
        if c[i]=='R':x+=d
        if c[i]=='U':y+=d
        if c[i]=='D':y-=d
    print(x,y)

ans=[]
for x,y in xyl:
    if (x+y)%2==0:
        x-=1
        res=solve(x,y)
        res.append('R')
        print(''.join(res))
        # check(res)
    else:
        res=solve(x,y)
        print(''.join(res))
        # check(res)

    
    
