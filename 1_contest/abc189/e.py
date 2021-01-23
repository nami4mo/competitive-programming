class Point:
    def __init__(self):
        self.flip=False
        self.x=1 #+-
        self.y=1 # +-
        self.xp=0
        self.yp=0
        
    def flip_x(self):
        self.x*=-1
        self.xp*=-1
    def flip_y(self):
        self.y*=-1
        self.yp*=-1

n=int(input())
xyl=[]
for _ in range(n):
    x,y=map(int, input().split())
    xyl.append((x,y))

ops=[]
m=int(input())
for _ in range(m):
    op=list(map(int, input().split()))
    ops.append(op)

qs=[[] for _ in range(m+1)]
q=int(input())
for i in range(q):
    a,b=map(int, input().split())
    qs[a].append((b,i))

ansl=[0]*(q)
for b,i in qs[0]:
    x,y=xyl[b-1]
    ansl[i]=(x,y)

point=Point()
for i in range(m):
    op=ops[i]
    if op[0]==1:
        if not point.flip:
            point.flip_x()
            point.flip=True
        else:
            point.flip_y()
            point.flip=False
    elif op[0]==2:
        if not point.flip:
            point.flip_y()
            point.flip=True
        else:
            point.flip_x()
            point.flip=False
    elif op[0]==3:
        p=op[1]
        if not point.flip:
            point.flip_x()
            point.xp+=2*p
        else:
            point.flip_y()
            point.yp+=2*p
    else:
        p=op[1]
        if not point.flip:
            point.flip_y()
            point.yp+=2*p
        else:
            point.flip_x()
            point.xp+=2*p

    if qs[i+1]:
        for b,qi in qs[i+1]:
            x,y=xyl[b-1]
            x*=point.x
            x+=point.xp
            y*=point.y
            y+=point.yp
            if not point.flip:
                ansl[qi]=(x,y)
            else:
                ansl[qi]=(y,x)

for x,y in ansl:print(x,y)
