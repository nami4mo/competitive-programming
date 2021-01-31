n,a,b=map(int, input().split())
sl=[int(input()) for _ in range(n)]
diff=max(sl)-min(sl)
if diff==0:
    print(-1)
    exit()

ave=sum(sl)/n
p=b/diff
ave*=p
q=a-ave
print(p,q)