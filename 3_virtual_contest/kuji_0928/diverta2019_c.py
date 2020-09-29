n = int(input())
ba_cnt = 0
b_top_cnt = 0
a_end_cnt = 0

ab = 0
for _ in range(n):
    s = input()
    ab += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        ba_cnt += 1
    elif s[0] == 'B':
        b_top_cnt += 1
    elif s[-1] == 'A':
        a_end_cnt += 1

ans = ab
if ba_cnt == 0:
    ans += min(a_end_cnt, b_top_cnt)
else:
    ans += (ba_cnt-1)
    if a_end_cnt >0:
        a_end_cnt -= 1
        ans += 1
    if b_top_cnt > 0:
        b_top_cnt -= 1
        ans += 1
    ans += min(a_end_cnt,b_top_cnt)

print(ans)

