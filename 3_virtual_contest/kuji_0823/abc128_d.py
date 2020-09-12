n,k = map(int, input().split())
vl = list(map(int, input().split()))    

ans = 0
ab_max = min(n,k)
for l in range(ab_max+1):
    for r in range(ab_max+1):
        if l+r > k: continue
        if l > n-r: continue
        ls = vl[:l]
        rs = vl[n-r:]
        # print(ls,rs)
        vals = ls + rs
        rem = k-(l+r)
        # print(rem)
        vals.sort()
        curr_sum = sum(vals)
        for i in range(rem):
            if i >= len(vals): break
            if vals[i] < 0: curr_sum -= vals[i]
            else: break
        # print(curr_sum)
        ans = max(ans,curr_sum)

print(ans)
        