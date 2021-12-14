n,q=map(int, input().split())
al=list(map(int, input().split()))

al.sort()
from bisect import bisect_left, bisect_right

for _ in range(q):
    x=int(input())
    cnt = n - bisect_left(al, x)
    print(cnt)
