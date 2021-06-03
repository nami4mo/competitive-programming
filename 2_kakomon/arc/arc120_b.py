h,w=map(int, input().split())
sl=[list(input()) for _ in range(h)]

ans=1
MOD=998244353
for i in range(0,h+w-1):
    r=False
    b=False
    for y in range(h):
        x=i-y
        if not 0<=x<w:continue
        if sl[y][x]=='B':b=True
        if sl[y][x]=='R':r=True
    #     print(y,x)
    # print(r,b)
    # print()
    if r and b:
        print(0)
        exit()
    if r or b:
        ans*=1
    else:
        ans*=2
        ans%=MOD
print(ans)