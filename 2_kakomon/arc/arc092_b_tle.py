from bisect import bisect_left, bisect_right

n=int(input())
aal=list(map(int, input().split()))
bbl=list(map(int, input().split()))

ans=0
for bit in range(29):
    bit2=pow(2,bit)
    mod=bit2*2
    al=[a%mod for a in aal]
    bl=[b%mod for b in bbl]
    # al.sort()
    bl.sort()
    l1=bit2
    r1=l1*2-1
    l2,r2=l1+mod,r1+mod
    cnt=0
    # print(l1,r1,l2,r2)
    for a in al:
        # for l,r in [(l1,r1),(l2,r2)]:
        rc=bisect_right(bl,r1-a)
        lc=bisect_right(bl,l1-a-1)
        cnt+=(rc-lc)
        rc=bisect_right(bl,r2-a)
        lc=bisect_right(bl,l2-a-1)
        cnt+=(rc-lc)
    # print('---')
    # print(bit,cnt)
    # print(al,bl)
    if cnt%2==1:ans+=bit2

print(ans)