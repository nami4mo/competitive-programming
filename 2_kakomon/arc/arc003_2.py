n=int(input())
sl=[input()[::-1] for _ in range(n)]
sl.sort()

for s in sl:
    print(s[::-1])