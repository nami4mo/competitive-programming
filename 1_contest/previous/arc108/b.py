from collections import deque
from sys import int_info

n = int(input())    
s = input()
q = deque([])
for si in s:
    q.append(si)
    if len(q) >= 3:
        if q[-3] == 'f' and q[-2] == 'o' and q[-1] == 'x':
            q.pop()
            q.pop()
            q.pop()
        
print(len(q))