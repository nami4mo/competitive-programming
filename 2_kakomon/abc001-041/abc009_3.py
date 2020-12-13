from collections import deque
n,k=map(int, input().split())
s=input()
sl=list(s)
sl.sort()
# q=deque(sl)
q=sl

alps = 'abcdefghijklmnopqrstuvwxyz'

top_diff_cnt = 0
ansl = []
for i in range(n):
    si = s[i]
    rem = s[i+1:]
    for j in range(len(q)):
        c_diff = 1 if si!=q[j] else 0
        orig_d = {chr(ord('a') + i): 0 for i in range(26)}
        back_d = {chr(ord('a') + i): 0 for i in range(26)}
        for c in rem:
            orig_d[c]+=1
        for m in range(len(q)):
            if m==j: continue
            back_d[q[m]]+=1
        back_same = 0
        for c in alps:
            back_same += min(orig_d[c], back_d[c])
        back_diff = n-i-1 - back_same
        if top_diff_cnt+c_diff+back_diff<=k:
            ansl.append(q[j])
            q.pop(j)
            top_diff_cnt += c_diff
            break

print(''.join(ansl))

