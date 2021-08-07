def apply(val):
    if '.' not in val:
        return int(val)*(10**4)
    else:
        top,bottom=val.split('.')
        top=int(top)*(10**4)
        need=4-len(bottom)
        bottom+='0'*need
        return top+int(bottom)


def gety(x,r,y):
    ok, ng = 0, 10**11
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if mid**2<=r**2-x**2:
            ok = mid
        else:
            ng = mid
    return ok


x,y,r=map(str, input().split())
x,y,r=apply(x),apply(y),apply(r)
x%=10**4
y%=10**4
# print(x,y,r)

STEP=10**4
left=x-r
if left%STEP!=0:
    left+=(STEP-left%STEP)

ans=0
cx=left
EPS=10**(-9)
while cx<=x+r:
    # print('--cx',cx)
    # ylen2=r**2-(x-cx)**2
    # print('y2',ylen2)
    # yl=ylen2**0.5
    # print('yl',yl)
    yl=gety(abs(x-cx),r,y)
    ytop=int(y+yl)
    ybottom=int(y-yl)
    if ytop%STEP!=0:
        ytop-=ytop%STEP
    if ybottom%STEP!=0:
        ybottom+=(STEP-ybottom%STEP)
    # print(ytop,ybottom)
    if ytop>=ybottom:
        ans+=(ytop-ybottom)//STEP+1
    # print('ans',ans)
    cx+=STEP

print(ans)