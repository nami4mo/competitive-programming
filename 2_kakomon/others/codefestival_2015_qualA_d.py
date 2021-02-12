def check(n,m,xl,k):
    done=0
    for x in xl:
        left_need=max(0,x-done-1)
        if left_need>k:return False
        if left_need==0:
            done=x+k
        elif left_need<=(k-2*left_need):
            done=x+k-2*left_need
        else:        
            done=x+(k-left_need)//2
    return done>=n

n,m=map(int, input().split())
xl=[int(input()) for _ in range(m)]

ng, ok = -1, 10**10+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    ok_flag = check(n,m,xl,mid)
    if ok_flag:
        ok = mid
    else:
    	ng = mid
print(ok)