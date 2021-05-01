n,k=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
cnt=0
for a,b in zip(al,bl):
    cnt+=abs(a-b)
if cnt<=k and (cnt-k)%2==0:
    print('Yes')
else:
    print('No')