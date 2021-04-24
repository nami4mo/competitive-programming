from typing import Deque


n,k=map(int, input().split())
s=input()
from collections import deque
d=[deque() for _ in range(26)]
for i,si in enumerate(s):
    c=ord(si)-ord('a')
    d[c].append(i)

ans=[]
pos=-1
for i in range(k):
    rem=k-i
    for c in range(26):
        while d[c] and d[c][0]<=pos:
            d[c].popleft()
        if not d[c]:continue
        cnt=n-d[c][0]
        if rem<=cnt:
            ans.append(chr(c+ord('a')))
            pos=d[c][0]
            break
print(''.join(ans))