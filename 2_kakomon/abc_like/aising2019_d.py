from bisect import bisect_left, bisect_right

n,q=map(int, input().split())
al=list(map(int, input().split()))
back_csums=[0]
cs=0
for a in al[::-1]:
    cs+=a
    back_csums.append(cs)

csums0=[0]
csums1=[0]
cs0,cs1=0,0
for i,a in enumerate(al):
    if i%2==1:
        cs0+=a
        csums0.append(cs0)
    else:
        cs1+=a
        csums1.append(cs1)

# print(csums0)
# print(csums1)

for _ in range(q):
    x=int(input())
    if x>=al[-1]:
        if n%2==0:
            print(csums0[n//2])
        else:
            print(csums1[n//2+1])
        continue

    ok, ng = 1, n+1
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        res = True
        # ...
        tak_cnt=(mid+1)//2
        ao_cnt=mid-tak_cnt
        tak_left=n-tak_cnt
        ao_max_diff=al[tak_left]-x
        # print('mid',mid,ao_max_diff)
        if ao_max_diff<0:
            ng=mid
            continue

        ao_left = bisect_left(al, x-ao_max_diff)
        res=(tak_left-ao_left>=ao_cnt)
        if res: ok = mid
        else: ng = mid

    tak_cnt=(ok+1)//2
    ao_cnt=ok-tak_cnt
    ans=back_csums[tak_cnt]
    left_cnt=n-ok
    if tak_cnt!=ao_cnt: left_cnt-=1
    if left_cnt%2==0:
        ans+=csums0[min(left_cnt//2, len(csums0)-1)]
    else:
        ans+=csums1[left_cnt//2+1]
    # print('--',ok,ans)
    print(ans)