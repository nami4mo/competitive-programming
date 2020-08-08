from collections import deque

n,m = map(int, input().split())
s = input()

s_seq_l = []
prev_s = '0'
cnt = 1
for s_i in s[1:-1]:
    if s_i == prev_s:
        cnt += 1
    else:
        s_seq_l.append((prev_s,cnt))
        cnt = 1
        prev_s = s_i
s_seq_l.append((prev_s,cnt))
s_seq_q = deque(s_seq_l)

ans = []
while True:
    remain = m
    poped = s_seq_q.pop()
    if poped[0][0] = '0':
        if remain < poped[0][1]:
            ans.append(remain)
            s_seq_q.append(('0',poped[0][1]-m))
        elif m == poped[0][1]:
            ans.append(remain)
    else:
        if 
