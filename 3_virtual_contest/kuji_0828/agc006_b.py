from collections import deque
n,x = map(int, input().split())

if x == 1 or x == 2*n-1:
    print('No')
    exit()

if x == 2:
    ansl = []
    q = deque()
    for i in range(5,2*n):
        q.append(i)
    for i in range(0,2*n-1):
        if i == n-2: ansl.append(3)
        elif i == n-1: ansl.append(2)
        elif i == n: ansl.append(1)
        elif i == n+1: ansl.append(4)
        else: ansl.append(q.pop())
        

else:
    ansl = []
    q = deque()
    fix = [x-1,x,x+1,x-2]
    for i in range(1,2*n):
        if i not in fix:
            q.append(i)
    for i in range(0,2*n-1):
        if i == n-2: ansl.append(x-1)
        elif i == n-1: ansl.append(x)
        elif i == n: ansl.append(x+1)
        elif i == n+1: ansl.append(x-2)
        else: ansl.append(q.pop())

print('Yes')
print(*ansl)