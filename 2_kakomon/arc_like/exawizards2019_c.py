n,q=map(int, input().split())
s=input()
ql=[]
for _ in range(q):
    t,d=input().split()
    ql.append((t,d))


def move(start,s,ql,n):
    pos=start
    for t,d in ql:
        if s[pos]==t:
            if d=='L':pos-=1
            else:pos+=1
        if pos<0: return -1
        if n<=pos: return 1
    return 0

ok, ng = -1, n
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    # ...
    if mid<0:
        pass
    else:
        moved=move(mid,s,ql,n)
        if moved==-1:res=True
        else:res=False
    if res: ok = mid
    else: ng = mid
left=ok


ng, ok = -1, n
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    # ...
    if mid<0:
        pass
    else:
        moved=move(mid,s,ql,n)
        if moved==1:res=True
        else:res=False
    if res: ok = mid
    else: ng = mid
right=ok

ans=right-left-1
print(ans)