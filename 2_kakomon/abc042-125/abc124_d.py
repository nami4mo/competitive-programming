from collections import deque

n,k = map(int, input().split())
s = input()

cnt_01 = []
prev = s[0]
cnt = 0
for c in s:
    if c != prev:
        cnt_01.append(cnt)
        cnt = 1
    else: 
        cnt += 1
    prev = c
else:
    cnt_01.append(cnt)


if len(cnt_01) <= 2*k:
    print(n)
    exit()


if s[0] == '0':
    ans_candi = sum(cnt_01[0:2*k])
    cnt_01 = cnt_01[1:]
else:
    ans_candi = 0


first_que = cnt_01[0:2*k+1]
que = deque(first_que)
curr_sum = sum(first_que)
ans = curr_sum
for i in range(k, len(cnt_01)-1):
    break_flag = False
    poped1 = que.popleft()
    poped2 = que.popleft()
    curr_sum -= (poped1 + poped2)
    if 2*i+1 < len(cnt_01):
        que.append(cnt_01[2*i+1])
        curr_sum += cnt_01[2*i+1]
    if 2*i+2 < len(cnt_01):
        que.append(cnt_01[2*i+2])
        curr_sum += cnt_01[2*i+2]
    else:
        break_flag = True
    ans = max(curr_sum, ans)
    if break_flag: break

print(max(ans,ans_candi))
