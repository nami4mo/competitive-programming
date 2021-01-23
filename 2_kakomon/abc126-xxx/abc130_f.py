xyld={}
xyl=[]
DIRS=['L','R','U','D']
for d in DIRS:
    xyld[d]=[]

xmax,xmax_d=-10**10,''
xmin,xmin_d=10**10,''
ymax,ymax_d=-10**10,''
ymin,ymin_d=10**10,''

n=int(input())
for i in range(n):
    x,y,d=map(str, input().split())
    x,y=int(x),int(y)
    xyld[d].append((x,y))
    xyl.append((x,y,d))
    if x>xmax:
        xmax,xmax_d=x,d
    if x<xmin:
        xmin,xmin_d=x,d
    if y>ymax:
        ymax,ymax_d=y,d
    if y<ymin:
        ymin,ymin_d=y,d

t_cands=[0]
for d in DIRS:
    xyld[d].sort()

from copy import deepcopy
xyldx=deepcopy(xyld)

if xmax_d=='U' or xmax_d=='D':
    if xyld['R']:
        dist=xmax-xyld['R'][-1][0]
        t_cands.append(dist)
elif xmax_d=='L':
    if xyld['R']:
        for i in range(len(xyld['R'])):
            x,y=xyld['R'][i]
            if x>xmax and i>0:
                dist=(xmax-xyld['R'][i-1][0])/2
                t_cands.append(dist)
                break
        else:
            dist=(xmax-xyld['R'][-1][0])/2
            t_cands.append(dist)
    if xyld['U']:
        for i in range(len(xyld['U'])):
            x,y=xyld['U'][i]
            if x>xmax and i>0:
                dist=(xmax-xyld['U'][i-1][0])
                t_cands.append(dist)
                break
        else:
            dist=(xmax-xyld['U'][-1][0])
            t_cands.append(dist)
    if xyld['D']:
        for i in range(len(xyld['D'])):
            x,y=xyld['D'][i]
            if x>xmax and i>0:
                dist=(xmax-xyld['D'][i-1][0])
                t_cands.append(dist)
                break
        else:
            dist=(xmax-xyld['D'][-1][0])
            t_cands.append(dist)


if xmin_d=='U' or xmin_d=='D':
    if xyld['L']:
        dist=xyld['L'][-1][0]-xmin
        t_cands.append(dist)
elif xmin_d=='R':
    if xyld['L']:
        for i in range(len(xyld['L'])):
            x,y=xyld['L'][i]
            if x>=xmin:
                dist=(xyld['L'][i][0]-xmin)/2
                t_cands.append(dist)
                break
    if xyld['U']:
        for i in range(len(xyld['U'])):
            x,y=xyld['U'][i]
            if x>=xmin:
                dist=(xyld['U'][i][0]-xmin)
                t_cands.append(dist)
                break
    if xyld['D']:
        for i in range(len(xyld['D'])):
            x,y=xyld['D'][i]
            if x>=xmin:
                dist=(xyld['D'][i][0]-xmin)
                t_cands.append(dist)
                break

# print(t_cands)

for d in DIRS:
    xyld[d].sort(key=lambda x: x[1])

if ymax_d=='R' or ymax_d=='L':
    if xyld['U']:
        dist=ymax-xyld['U'][-1][1]
        t_cands.append(dist)
elif ymax_d=='D':
    if xyld['U']:
        for i in range(len(xyld['U'])):
            x,y=xyld['U'][i]
            if y>ymax and i>0:
                dist=(ymax-xyld['U'][i-1][1])/2
                t_cands.append(dist)
                break
        else:
            dist=(ymax-xyld['U'][-1][1])/2
            t_cands.append(dist)
    if xyld['R']:
        for i in range(len(xyld['R'])):
            x,y=xyld['R'][i]
            if y>ymax and i>0:
                dist=(ymax-xyld['R'][i-1][1])
                t_cands.append(dist)
                break
        else:
            dist=(ymax-xyld['R'][-1][1])
            t_cands.append(dist)
    if xyld['L']:
        for i in range(len(xyld['L'])):
            x,y=xyld['L'][i]
            if y>ymax and i>0:
                dist=(ymax-xyld['L'][i-1][1])
                t_cands.append(dist)
                break
        else:
            dist=(ymax-xyld['L'][-1][1])
            t_cands.append(dist)


if ymin_d=='R' or ymin_d=='L':
    if xyld['D']:
        dist=xyld['D'][-1][1]-ymin
        t_cands.append(dist)
elif ymin_d=='U':
    if xyld['D']:
        for i in range(len(xyld['D'])):
            x,y=xyld['D'][i]
            if y>=ymin:
                dist=(xyld['D'][i][1]-ymin)/2
                t_cands.append(dist)
                break
    if xyld['R']:
        for i in range(len(xyld['R'])):
            x,y=xyld['R'][i]
            if y>=ymin:
                dist=(xyld['R'][i][1]-ymin)
                t_cands.append(dist)
                break
    if xyld['L']:
        for i in range(len(xyld['L'])):
            x,y=xyld['L'][i]
            if y>=ymin:
                dist=(xyld['L'][i][1]-ymin)
                t_cands.append(dist)
                break

# print(t_cands)
ans=10**18
for t in t_cands:
    if t<0:continue
    xmax=-10**10
    xmin=10**10
    ymax=-10**10
    ymin=10**10
    if xyldx['R']:
        x=xyldx['R'][-1][0]+t
        xmax=max(xmax,x)
        x=xyldx['R'][0][0]+t
        xmin=min(xmin,x)
    if xyldx['L']:
        x=xyldx['L'][-1][0]-t
        xmax=max(xmax,x)
        x=xyldx['L'][0][0]-t
        xmin=min(xmin,x)
    if xyldx['U']:
        x=xyldx['U'][-1][0]
        xmax=max(xmax,x)
        x=xyldx['U'][0][0]
        xmin=min(xmin,x)
    if xyldx['D']:
        x=xyldx['D'][-1][0]
        xmax=max(xmax,x)
        x=xyldx['D'][0][0]
        xmin=min(xmin,x)

    if xyld['R']:
        y=xyld['R'][-1][1]
        ymax=max(ymax,y)
        y=xyld['R'][0][1]
        ymin=min(ymin,y)
    if xyld['L']:
        y=xyld['L'][-1][1]
        ymax=max(ymax,y)
        y=xyld['L'][0][1]
        ymin=min(ymin,y)
    if xyld['U']:
        y=xyld['U'][-1][1]+t
        ymax=max(ymax,y)
        y=xyld['U'][0][1]+t
        ymin=min(ymin,y)
    if xyld['D']:
        y=xyld['D'][-1][1]-t
        ymax=max(ymax,y)
        y=xyld['D'][0][1]-t
        ymin=min(ymin,y)
    v=(xmax-xmin)*(ymax-ymin)
    ans=min(ans,v)
print(ans)