from bisect import bisect_left, bisect_right

n, m = map(int, input().split()) 
al = list(map(int, input().split())) 

sushi_max_l = [0]*n
for a in al:
    a_minus = a*(-1)
    # a_minusより大きい最小要素のindex（a未満の最大要素のindex）
    ind = bisect_right(sushi_max_l, a_minus)
    if ind == n:
        print(-1)
    else:
        print(ind+1)
        sushi_max_l[ind] = a_minus

