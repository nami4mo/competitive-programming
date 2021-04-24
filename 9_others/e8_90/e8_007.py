from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n=int(input())
al=[-10**18]+list(map(int, input().split()))+[10**18]
al.sort()
for _ in range(int(input())):
    b=int(input())
    ind = bisect_right(al,b)-1
    d=abs(b-al[ind])
    ind = bisect_left(al, b)
    d=min(d,abs(b-al[ind]))
    print(d)