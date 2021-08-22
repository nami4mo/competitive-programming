from collections import deque
def s2i(s):
    res=0
    for i in range(3):
        val=0
        si=s[i]
        if 'a'<=si<='z':val=ord(si)-ord('a')
        else:val=ord(si)-ord('A')+26
        res+=52**(2-i)*val
    return res

n=int(input())
nn=52**3

edges=[]
glr=[list() for _ in range(nn)]
rems=[0]*nn
for _ in range(n):
    s=input()
    vf=s2i(s[:3])
    vb=s2i(s[-3:])
    edges.append((vf,vb))
    glr[vb].append(vf)
    rems[vf]+=1

res=[-1]*nn # -1:TBD, 0:lose, 1:win
q=deque()
for i in range(nn):
    if rems[i]==0:
        res[i]=0
        q.append(i)

while q:
    poped=q.popleft()
    for neib in glr[poped]:
        # print(poped,neib)
        if res[neib]!=-1:continue
        rems[neib]-=1
        if res[poped]==0:
            q.append(neib)
            res[neib]=1
        elif rems[neib]==0:
            q.append(neib)
            res[neib]=0


for i in range(n):
    ss=edges[i][1]
    if res[ss]==-1:print('Draw')
    elif res[ss]==0:print('Takahashi')
    else:print('Aoki')
