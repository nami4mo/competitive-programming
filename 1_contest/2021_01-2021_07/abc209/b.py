n,x=map(int, input().split())
al=list(map(int, input().split()))
v=0
for i in range(n):
    v+=al[i]
    if i%2==1:v-=1
if x>=v:print('Yes')
else:print('No')