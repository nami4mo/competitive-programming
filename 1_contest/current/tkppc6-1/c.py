n=int(input())
al=list(map(int, input().split()))
bl=[]
cnt=0
for a in al:
    if a==-1:cnt+=1
    else:bl.append(a)

bl.sort()
mi=10000000
ma=-1
for i in range(len(bl)):
    if al[0]==bl[i]:
        ind=i+1
        mi=min(i+1,mi)
        ma=max(i+1,ma)
# print(mi,ma)
if n<mi:
    print('No')
    exit()
if mi<=n<=ma:
    print('Yes')
    exit()
d=min(abs(n-ma),abs(n-mi))
if d<=cnt:
    print('Yes')
else:
    print('No')