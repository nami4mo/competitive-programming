p,q,r,k=map(int, input().split())
p%=10
q%=10
r%=10

MAX=10**3
gl=[-1]*MAX
for a1 in range(10):
    for a2 in range(10):
        for a3 in range(10):
            a0=(a1+a2+a3)%10
            val_f=a1*100+a2*10+a3
            val_t=a2*100+a3*10+a0
            gl[val_f]=val_t

from math import log2
logk = int(log2(k))+1
db = [ [0]*MAX for _ in range(logk) ]
for ni in range(MAX): 
    db[0][ni] = gl[ni]
for ki in range(logk-1):
    for ni in range(MAX):
        db[ki+1][ni] = db[ki][db[ki][ni]]

# k=3
# k-=1
# k+=2
# k-=3
k-=1
now = p*100+q*10+r
for i in range(logk):
    if k&(1<<i) > 0:
        now = db[i][now]
print(now//100)
# print(now)