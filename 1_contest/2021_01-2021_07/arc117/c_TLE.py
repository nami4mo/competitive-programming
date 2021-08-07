def get(l,r):
    if l==r:return l
    if l!='B' and r!='B':return 'B'
    if l!='R' and r!='R':return 'R'
    if l!='W' and r!='W':return 'W'

def c012(l,r):
    if l==r:return l
    if l!=0 and r!=0:return 0
    if l!=1 and r!=1:return 1
    if l!=2 and r!=2:return 2

n=int(input())
cl=list(input())

REP=12
from itertools import product

p3=[]
for i in range(REP):
    p3.append(pow(3,i))

c2c=[['']*(3**REP) for _ in range(REP+1)]
c2c[1][0]='B'
c2c[1][1]='R'
c2c[1][2]='W'

for rlen in range(2,REP+1):
    ite = list(product(range(3),repeat=rlen))
    for pattern in ite:
        val=0
        for i, v in enumerate(pattern):
            val+=p3[i]*v

        next_val=0
        for i in range(len(pattern)-1):
            vv=c012(pattern[i],pattern[i+1])
            next_val+=p3[i]*vv

        c2c[rlen][val]=c2c[rlen-1][next_val]

c2cr=c2c[REP][:]
while len(cl)>=REP:
    ss=[]
    clen=len(cl)
    loop=clen-REP+1
    val=0
    for i in range(REP):
        c=cl[i]
        # if s[j]=='B':val
        if c=='R': val+=p3[REP-i-1]*1
        if c=='W': val+=p3[REP-i-1]*2
    ss.append(c2cr[val])

    # print(val)
    for i in range(loop-1):
        pop=cl[i]
        ins=cl[i+REP]
        if pop=='R': val-=p3[REP-1]*1
        if pop=='W': val-=p3[REP-1]*2
        val*=3
        if ins=='R': val+=1
        if ins=='W': val+=2
        # print(val)
        ss.append(c2cr[val])
    cl=ss[:]

cn=len(cl)
for i in range(cn-1):
    ss=[]
    for j in range(len(cl)-1):
        c=get(cl[j],cl[j+1])
        ss.append(c)
    cl=ss[:]
print(cl[0])