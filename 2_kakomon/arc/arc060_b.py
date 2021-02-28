from math import log
def to_b_basenum(n,b):
    v=n
    res=[]
    while v>0:
        rem=v%b
        res.append(rem)
        v//=b
    return res

n=int(input())
s=int(input())
for b in range(2,int(n**0.5)+2):
    b_num=to_b_basenum(n,b)
    # if b%10==0: print(b,b_num)
    if sum(b_num)==s:
        print(b)
        # print('aa')
        exit()

for v2 in range(int(n**0.5)+2,0,-1):
    bmax=n//v2
    bmin=n//(v2+1)+1
    # print(v2,bmax,bmin)
    if bmax<=1:continue
    need_v1=s-v2
    if need_v1<0:continue
    bmin_v1=n%bmin
    dist=bmin_v1-need_v1
    if dist<0 or dist%v2!=0:continue
    d=dist//v2
    bans=bmin+d
    print(bans)
    # print(bmax,bmin,v2)
    exit()

if s==n:
    print(n+1)
else:
    print(-1)