n = int(input())
al = list(map(int, input().split()))
al.sort(reverse=True)
ali = 0
bob = 0
for i,a in enumerate(al):
    if i%2 == 0: ali += a
    else: bob += a

print(ali-bob)
