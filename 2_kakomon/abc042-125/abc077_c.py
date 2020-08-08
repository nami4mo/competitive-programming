from bisect import bisect_left, bisect_right
n = int(input())
al = list(map(int,input().split()))
bl = list(map(int,input().split()))
cl = list(map(int,input().split()))

al.sort()
bl.sort()
cl.sort()

ans = 0
for b in bl:
    # b未満の要素の個数
    a_cnt = bisect_left(al,b)
    # bより大きい要素の個数
    c_cnt = n - bisect_right(cl,b)
    ans += a_cnt*c_cnt

print(ans)