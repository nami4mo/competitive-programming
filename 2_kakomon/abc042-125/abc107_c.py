n,k = map(int, input().split())
xl = list(map(int, input().split()))
xl.sort()

# zero確認
ind = bisect_right(al, 0) - 1
ind = ind if 0 <= ind < N else None
val = al[ind] if ind is not None else None
zero_flag = (val == 0)

# b未満の要素の個数
cnt_nega = bisect_left(al, 0)
nega_l = xl[0:cnt_nega]

# bより大きい要素の個数
cnt_posi = N - bisect_right(al, 0)
if cnt_posi > 0:
    posi_l = xl[-cnt_posi:]
else:
    posi_l = []

ans = 10**9
for left in range(1,k+1):
    left_d = 