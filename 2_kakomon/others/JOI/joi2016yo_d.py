from bisect import bisect_left, bisect_right

n,t,q=map(int, input().split())
adl=[]
for _ in range(n):
    a,d=map(int, input().split())
    adl.append((a,d))

prev_d=0
prev_a=0
walls=[]
for a,d in adl:
    if prev_d==1 and d==2:
        wall=(prev_a+a)//2
        walls.append(wall)
    prev_d=d
    prev_a=a

ansl=[]
for _ in range(q):
    a,d=adl[int(input())-1]
    if d==1:
        ind = bisect_left(walls, a)
        if ind==len(walls):
            ans=a+t
            ansl.append(ans)
        else:
            ans=min(walls[ind],a+t)
            ansl.append(ans)
    else:
        ind = bisect_right(walls, a)-1
        if ind==-1:
            ans=a-t
            ansl.append(ans)
        else:
            ans=max(walls[ind],a-t)
            ansl.append(ans)

for a in ansl:print(a)

