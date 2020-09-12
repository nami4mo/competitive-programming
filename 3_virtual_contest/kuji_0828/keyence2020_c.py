n,k,s = map(int, input().split())
if s == 10**9:
    ansl = []
    for i in range(n):
        if i < k:
            ansl.append(s)
        else:
            ansl.append(1)
    print(*ansl)

else:
    ansl = []
    for i in range(n):
        if i < k:
            ansl.append(s)
        else:
            ansl.append(10**9)
    print(*ansl)