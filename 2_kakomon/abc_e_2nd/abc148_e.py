n=int(input())
cnt2=0
cnt5=0

if n%2==1:
    print(0)
    exit()

v2=2
while v2<=n:
    cnt=n//v2
    cnt2+=cnt
    v2*=2

v5=5
while v5*2<=n:
    cnt=n//(v5*2)
    cnt5+=cnt
    v5*=5

ans=min(cnt2,cnt5)
print(ans)