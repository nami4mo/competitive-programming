from bisect import bisect_left, bisect_right

n,k = map(int, input().split())
vl = list(map(int, input().split()))

ans = 0
for get_num in range(0,k+1):
    rem = k-get_num
    for l in range(0,get_num+1):
        r = get_num-l
        if l+r > n: continue
        ls = vl[:l]
        rs = vl[n-r:]
        curr_l = ls + rs
        curr_l.sort()
        minus_cnt = bisect_left(curr_l, 0)
        if minus_cnt <= rem:
            curr_ans = sum(curr_l[minus_cnt:])
            ans = max(curr_ans,ans)
        else:
            curr_ans = sum(curr_l[rem:])
            ans = max(curr_ans,ans)

print(ans)