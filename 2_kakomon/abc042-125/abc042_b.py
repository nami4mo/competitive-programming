n,l = map(int, input().split())
sl = []
for _ in range(n):
    sl.append(input())

sl.sort()
print(''.join(sl))