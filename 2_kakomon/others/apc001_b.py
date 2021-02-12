from math import ceil

n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
diff = sum(bl)-sum(al)
need = 0
for i in range(n):
    need += max(0, ceil((bl[i]-al[i])/2) )

if need <= diff:
    print('Yes')
else:
    print('No')