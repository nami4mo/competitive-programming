s=input()
t=int(input())

from collections import Counter
c=Counter(s)
x=c['U']-c['D']
y=c['R']-c['L']
d=abs(x)+abs(y)
if t==1:
    ans=d+c['?']
    print(ans)
else:
    ans=d-c['?']
    if ans>=0: print(ans)
    else:
        if ans%2==0:print(0)
        else:print(1)