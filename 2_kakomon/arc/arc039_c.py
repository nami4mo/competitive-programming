k=int(input())
s=input()
dl={(0,0):(-1,0)}
dr={(0,0):(1,0)}
du={(0,0):(0,1)}
dd={(0,0):(0,-1)}

px,py=0,0
for si in s:
    if si=='R':
        pxx,pyy=px+1,py
        if (pxx,pyy) in dr:
            pxx,pyy=dr[(pxx,pyy)]
    if si=='L':
        pxx,pyy=px-1,py
        if (pxx,pyy) in dl:
            pxx,pyy=dl[(pxx,pyy)]
    if si=='U':
        pxx,pyy=px,py+1
        if (pxx,pyy) in du:
            pxx,pyy=du[(pxx,pyy)]
    if si=='D':
        pxx,pyy=px,py-1
        if (pxx,pyy) in dd:
            pxx,pyy=dd[(pxx,pyy)]
    

    if (pxx-1,pyy) in dl: dl[(pxx,pyy)]=dl[(pxx-1,pyy)]
    else: dl[(pxx,pyy)]=(pxx-1,pyy)

    if (pxx+1,pyy) in dr: dr[(pxx,pyy)]=dr[(pxx+1,pyy)]
    else: dr[(pxx,pyy)]=(pxx+1,pyy)

    if (pxx,pyy-1) in dd: dd[(pxx,pyy)]=dd[(pxx,pyy-1)]
    else: dd[(pxx,pyy)]=(pxx,pyy-1)

    if (pxx,pyy+1) in du: du[(pxx,pyy)]=du[(pxx,pyy+1)]
    else: du[(pxx,pyy)]=(pxx,pyy+1)

    cx,cy=dr[(pxx,pyy)]
    dl[ (cx-1,cy) ] = dl[(pxx,pyy)]

    cx,cy=dl[(pxx,pyy)]
    dr[ (cx+1,cy) ] = dr[(pxx,pyy)]

    cx,cy=du[(pxx,pyy)]
    dd[ (cx,cy-1) ] = dd[(pxx,pyy)]

    cx,cy=dd[(pxx,pyy)]
    du[ (cx,cy+1) ] = du[(pxx,pyy)]

    if si=='R': 
        dl[(pxx,pyy)]=dl[(px,py)]
        dr[(px,py)]=dr[(pxx,pyy)]
    if si=='L': 
        dr[(pxx,pyy)]=dr[(px,py)]
        dl[(px,py)]=dl[(pxx,pyy)]
    if si=='U': 
        dd[(pxx,pyy)]=dd[(px,py)]
        du[(px,py)]=du[(pxx,pyy)]
    if si=='D': 
        du[(pxx,pyy)]=du[(px,py)]
        dd[(px,py)]=dd[(pxx,pyy)]

    px,py=pxx,pyy

print(px,py)