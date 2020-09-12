n = int(input())
last_a_cnt = 0
top_b_cnt = 0
last_a_top_b_cnt = 0
ab_cnt = 0

for _ in range(n):
    s = input()
    ab_cnt += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A': last_a_top_b_cnt += 1
    elif s[0] == 'B' and s[-1] != 'A': top_b_cnt += 1
    elif s[0] != 'B' and s[-1] == 'A': last_a_cnt += 1


if last_a_cnt > 0:
    ans = 0
    last_a_cnt -= 1
    ans += last_a_top_b_cnt    
    ans += min(last_a_cnt+1, top_b_cnt)
    ans += ab_cnt

else:
    ans = 0
    if last_a_top_b_cnt > 0:
        ans += (last_a_top_b_cnt-1)
        ans += min(1, top_b_cnt)
    ans += ab_cnt

print(ans)