import sys
input = sys.stdin.readline

n,m=map(int, input().split())
gl=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

neib_cnts=[0]*n
for i in range(n):
    neib_cnts[i]=len(gl[i])

thre=int(m**0.5)
gl_many=[[] for _ in range(n)]
for i in range(n):
    for neib in gl[i]:
        if neib_cnts[neib]>thre:
            gl_many[i].append(neib)

cs=[(1,-1)]*n # (color, q_ind)
changes=[(1,-1)]*n # (color, q_ind)

al=[]
q=int(input())
for i in range(q):
    x,y=map(int, input().split())
    x-=1
    color,qi=cs[x]
    for neib in gl_many[x]:
        nc,nqi=changes[neib]
        if nqi>qi:
            color=nc
            qi=nqi
    # cs[x]=(color,qi)
    al.append(color)
    cs[x]=(y,i)

    if neib_cnts[x]>thre:
        changes[x]=(y,i)
    else:
        for neib in gl[x]:
            cs[neib]=(y,i)

for a in al:print(a)