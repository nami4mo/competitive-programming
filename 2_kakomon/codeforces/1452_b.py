ansl=[]
for _ in range(int(input())):
    n=int(input())
    al=list(map(int, input().split()))
    ma=max(al)
    need_min=ma*(n-1)
    s=sum(al)
    need=s
    rem=s%(n-1)
    if rem!=0: need+=(n-1-rem)
    need=max(need,need_min)
    ans=need-s
    ansl.append(max(0,ans))
for a in ansl:print(a)