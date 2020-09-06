t=int(input())
for _ in range(t):
    a,b,x,y,n = map(int, input().split())
    if x < y:
        a,b = b,a
        x,y = y,x
    if a-x+b-y <= n:
        print(x*y)
    else:
        absum = a+b-n
        amin = max(a-n,x)
        bmin = max(b-n,y)
        abmin = min(amin,bmin)
        ans = (absum-abmin)*abmin
        print(ans)
        # if b-y < n:
        #     rem = n-(b-y)
        #     a -= rem
        #     print(a*y)
        # else:

    