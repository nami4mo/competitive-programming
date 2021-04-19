n=int(input())
mins=[]
maxs=[]
for _ in range(n):
    a,b=map(int, input().split())
    if n%2==0: a,b=a*2,b*2
    mins.append(a)
    maxs.append(b)
mins.sort()
maxs.sort()

if n%2==1:
    c1=mins[n//2]
    c2=maxs[n//2]
    cnt=c2-c1+1
    print(cnt)
else:
    c1=(mins[n//2-1]+mins[n//2])//2
    c2=(maxs[n//2-1]+maxs[n//2])//2
    cnt=c2-c1+1
    print(cnt)
    