n,l=map(int, input().split())
al=list(map(int, input().split()))

# ok, ng = 0, 10**9+1
ok, ng = 0, 10
while abs(ok-ng) > 1:
    mid = (ok+ng)//2

    # mid ~ l
    curr=0
    ok_flag=True
    print('---',mid)
    for a in al:
        print(curr)
        if curr+a<=l:
            curr+=a
        else:
            if curr<mid:
                ok_flag=False
                break
            curr=a
            if curr<mid:
                ok_flag=False
                break
    if ok_flag:
        ok = mid
    else:
    	ng = mid
print(ok)