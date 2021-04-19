h,w=map(int, input().split())
sl=[]
for _ in range(h):
    row=list(input())
    sl.append(row)

row_black_st=[set() for _ in range(h)]
col_black_st=[set() for _ in range(w)]

for i in range(h):
    for j in range(w):
        if sl[i][j]=='#':
            row_black_st[i].add(j)
            col_black_st[j].add(i)

ans=0
from collections import deque
q=deque()

r_rem,c_rem=h,w
r_used=[False]*h
c_used=[False]*w

for i in range(h):
    l=len(row_black_st[i])
    if l==0 or l==w:
        # ans+=1
        # r_rem-=1
        q.append(('r',i)) 
        r_used[i]=True

for j in range(w):
    l=len(col_black_st[j])
    if l==0 or l==h:
        # ans+=1
        # c_rem-=1
        q.append(('c',j)) 
        c_used[j]=True


while q:
    rc,ind=q.popleft()
    ans+=1
    if rc=='r':
        r_rem-=1
        for j in range(w):
            if c_used[j]: continue
            col_black_st[j].discard(ind)
            l=len(col_black_st[j])
            if l==0 or l==r_rem:
                q.append(('c',j))
                c_used[j]=True

    if rc=='c':
        c_rem-=1
        for i in range(h):
            if r_used[i]: continue
            row_black_st[i].discard(ind)
            l=len(row_black_st[i])
            if l==0 or l==c_rem:
                q.append(('r',i))
                r_used[j]=True
print(ans)