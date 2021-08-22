n,k = map(int, input().split())
s = input()

rl_cnt = 0
for s1,s2 in zip(s[:-1],s[1:]):
    if s1 == 'R' and s2 == 'L':
        rl_cnt += 1

left_happy = 1 if s[0] == 'R' else 0
right_happy = 1 if s[-1] == 'L' else 0

first_happy = n - rl_cnt*2 -2 + left_happy + right_happy
# print(first_happy)
if k <= rl_cnt:
    ans = first_happy + k*2
else:
    rem = k-rl_cnt
    ans = first_happy + rl_cnt*2 + min(rem, 2-left_happy+right_happy)

print(min(ans,n-1))