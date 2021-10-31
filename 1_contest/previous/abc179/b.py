n=int(input())

cnt = 0
ans = False
for _ in range(n):
    a,b = map(int, input().split())
    if a == b:
        cnt += 1
    else:
        cnt = 0
    if cnt == 3:
        ans = True

if ans: print('Yes')
else: print('No')