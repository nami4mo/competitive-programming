n=int(input())

def rot(sl):
    res=[['.']*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            val=sl[i][j]
            res[n-1-j][i]=val
    return res

def check(sl,tl):
    s_sy,s_sx=-1,-1
    for x in range(n):
        for y in range(n):
            if sl[y][x]=='#':
                s_sx=x
                break
        if s_sx!=-1:break

    for y in range(n):
        for x in range(n):
            if sl[y][x]=='#':
                s_sy=y
                break
        if s_sy!=-1:break
    

    t_sy,t_sx=-1,-1
    for x in range(n):
        for y in range(n):
            if tl[y][x]=='#':
                t_sx=x
                break
        if t_sx!=-1:break
        
    for y in range(n):
        for x in range(n):
            if tl[y][x]=='#':
                t_sy=y
                break
        if t_sy!=-1:break

    for dy in range(n):
        for dx in range(n):
            sy=s_sy+dy
            sx=s_sx+dx
            ty=t_sy+dy
            tx=t_sx+dx
            sval='.'
            tval='.'
            if 0<=sy<n and 0<=sx<n and sl[sy][sx]=='#':
                sval='#'
            if 0<=ty<n and 0<=tx<n and tl[ty][tx]=='#':
                tval='#'
            if sval!=tval:
                return False
    return True

sl=[ list(input()) for _ in range(n)]
tl=[ list(input()) for _ in range(n)]
for _ in range(4):
    ress=check(sl,tl)
    if ress:
        print('Yes')
        exit()
    sl=rot(sl)
print('No')

