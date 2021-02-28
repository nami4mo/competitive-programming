al=[]
for _ in range(int(input())):
    n,k=map(int, input().split())
    if k<=n:
        if n%k==0: al.append(1)
        else: al.append(2)
        continue
    ans=(k-1)//n+1
    al.append(ans)
for a in al:print(a)