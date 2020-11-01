n,z,w = map(int, input().split())
al = list(map(int, input().split()))
if n == 1:
    print(abs(al[0]-w))
else:
    ans1 = abs(al[-1]-w)
    ans2 = abs(al[-1]-al[-2])
    print(max(ans1,ans2))