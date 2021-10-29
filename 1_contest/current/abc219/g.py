import sys
input = sys.stdin.readline

n,m,q=map(int, input().split())
gl=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)
xl=list(map(int, input().split()))

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
for i in range(n):
    cs[i]=(i+1,-1)
    changes[i]=(i+1,-1)

al=[]
# q=int(input())
# for i in range(q):
for i,x in enumerate(xl):
    x-=1
    # x,y=map(int, input().split())
    color,qi=cs[x]
    for neib in gl_many[x]:
        nc,nqi=changes[neib]
        if nqi>qi:
            color=nc
            qi=nqi
    # cs[x]=(color,qi)
    # al.append(color)
    cs[x]=(color,i)
    if neib_cnts[x]>thre:
        # print(x+1)
        changes[x]=(color,i)
    else:
        for neib in gl[x]:
            cs[neib]=(color,i)

# print(cs)
# print(changes)
ansl=[]
for i in range(n):
    # if neib_cnts[i]>thre:
    color,qi=cs[i]
    for neib in gl_many[i]:
        # print('---',i,neib)
        nc,nqi=changes[neib]
        # print(nqi,qi)
        if nqi>qi:
            color=nc
            qi=nqi
    # print(color)
    ansl.append(color)
    # else:
    #     print(cs[i][0])

print(*ansl)