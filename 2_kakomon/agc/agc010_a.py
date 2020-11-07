n = int(input())
al = list(map(int, input().split()))
if sum(al)%2 == 0: print('YES')
else: print('NO')