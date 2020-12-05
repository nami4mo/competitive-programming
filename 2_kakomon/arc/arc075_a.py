n=int(input())
nottens=[]
ans=0
for _ in range(n):
    s=int(input())
    ans+=s
    if s%10!=0: nottens.append(s)

if ans%10!=0:
    print(ans)
else:
    nottens.sort()
    if nottens:
        ans -= nottens[0]
    else:
        ans = 0
    print(ans)