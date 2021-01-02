from collections import deque

n=int(input())
s=input()
t=input()

if t[0]!=t[2]:
    # print(s.count(t))
    # exit()
    # s=list(s)
    ans=0
    while True:
        ind = s.find(t)
        if ind<0:break
        ans+=1
        s=s[:ind]+s[ind+3:]
    print(ans)
    exit()

if t[0]==t[1] and t[1]==t[2]:
    al=list(s)
    cntl = []
    prev = al[0]
    cnt = 1
    for a in al[1:]:
        if prev == a: cnt+=1
        else:
            cntl.append((prev,cnt))
            cnt = 1
            prev = a
    cntl.append((prev,cnt))
    ans=0
    for val,cnt in cntl:
        if val==t[0]:
            ans+=cnt//3
    print(ans)
    print(cntl)
    exit()

mid=t[1]
fb=t[0] # = t[2]
t2=t[0:2]
s=s.replace(t2,'X')
# print(s)

ans=0
# q=deque()
fcnt=0
xcnt=0
for si in s:
    if si=='X':
        xcnt+=1
    elif si==fb:
        if xcnt>0:
            if xcnt==2 and fcnt>=1:
                xcnt-=2
                fcnt-=1
                ans+=2
            else:
                xcnt-=1
                ans+=1
        else:
            fcnt+=1
    else:
        ans+=(xcnt*2//4)
        xcnt=0
        fcnt=0
    print('')
    print('xcnt',xcnt)
    print('fcnt',fcnt)
    print(ans)

print(s)
# ns=''
# ns+=(fcnt)*fcnt
# ns+=(t2)*xcnt

if xcnt>=2:
    ans+=1
    xcnt-=1
    m=min(fcnt,xcnt-1)
    ans+=m
    xcnt-=m
ans+=(xcnt*2//4)
print(ans)