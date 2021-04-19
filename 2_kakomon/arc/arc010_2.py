n=int(input())

from collections import deque

ends=[0,31,29,31,30,31,30,31,31,30,31,30,31]
starts=[0]
for i in range(12):
    starts.append(starts[i]+ends[i])
date=[False]*366

for i in range(366):
    if i%7==0 or i%7==6:
        date[i]=True

hs=[]
for _ in range(n):
    md=input()
    m,d=md.split('/')
    m,d=int(m),int(d)
    day=starts[m]+d-1
    hs.append(day)

hs.sort()
for day in hs:
    for i in range(366):
        if day+i>=366:break
        if not date[day+i]:
            date[day+i]=True
            break
# print(date[:36])
ans=0
c=0
for i in range(366):
    if date[i]:c+=1
    else:c=0
    ans=max(c,ans)
print(ans) 