n = int(input())
al = list(map(int, input().split()))

min_abs = 10**9
abs_sum = 0
minus_cnt = 0
zero_cnt = 0
for a in al:
    if a < 0: minus_cnt+=1
    elif a == 0: zero_cnt+=1
    abs_sum += abs(a)
    min_abs = min(min_abs, abs(a))

if minus_cnt%2 == 0:
    print(abs_sum)
else:
    if zero_cnt > 0:
        print(abs_sum)
    else:
        print(abs_sum-min_abs*2)
