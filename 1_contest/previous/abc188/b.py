n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
v=0
for i in range(n):
    v+=al[i]*bl[i]
if v==0:print('Yes')
else:print('No')