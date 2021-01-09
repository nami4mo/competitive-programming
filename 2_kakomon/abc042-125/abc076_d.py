n=int(input())
tl=list(map(int, input().split()))
vl=list(map(int, input().split()))
vl=[v*2 for v in vl]
from collections import deque
tll=[0]
csum=0
for t in tl:
    csum+=t*2
    tll.append(csum)
tq=deque(tll)
vq=deque(vl)
tn=tll[-1]
tmaxs=[0]*(tn+1)

# print(tq)
# print(vq)

cmax=0
tmaxs[tq.pop()]=0
cv=vq.pop()
for i in range(tn-1,0,-1):
    if i==tq[-1]:
        prev_cv=cv
        tq.pop()
        cv=vq.pop()

        cmax=min(cmax+1,cv,prev_cv)
        tmaxs[i]=cmax
        # print('----',i,cv,cmax)
    else:
        cmax=min(cmax+1,cv)
        tmaxs[i]=cmax

# vll=vl+[0]
# for i in range(n):
#     tmaxs[tll[i+1]]=min(vll[i+1],tmaxs[tll[i+1]])
    

# print(tmaxs)
# tq=deque(tll[1:])
ans=0
vel=0
prev_vel=0
for i in range(0,tn+1):
    vel=min(vel+1,tmaxs[i])
    # print(i,vel)

    ans+=(vel+prev_vel)/2
    prev_vel=vel
print(ans/4)
# print(tmaxs)