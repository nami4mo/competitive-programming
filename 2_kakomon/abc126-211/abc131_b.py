n,l = map(int, input().split())
al = list(range(l,l+n))
ans = sum(al)

if 0 in al:
    print(ans)
elif al[-1] <= 0:
    print(ans-al[-1])
else:
    print(ans-al[0])