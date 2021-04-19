n,k=map(int, input().split())
al=list(map(int, input().split()))
fl=list(map(int, input().split()))
al.sort()
fl.sort(reverse=True)

ng, ok = -1, 10**12+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    # ...
    rem=k
    for i in range(n):
        want=mid//fl[i]
        need=max(0,al[i]-want)
        rem-=need
    if rem>=0: ok = mid
    else: ng = mid
print(ok)