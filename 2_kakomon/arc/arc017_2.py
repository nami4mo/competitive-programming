import sys
input = sys.stdin.readline

n,k=map(int, input().split())
al=[int(input()) for _ in range(n)]
if k==1:
    print(n)
    exit()

ans=0
ok=True
ngi=0
for i in range(1,k):
    if al[i-1]>=al[i]:
        ngi=i+1
if ngi==0:ans+=1

for i in range(k,n):
    if al[i-1]>=al[i]:
        ngi=k
    else:
        ngi-=1
        if ngi<=1: 
            ans+=1
            # print(i)

print(ans)
# print(al)