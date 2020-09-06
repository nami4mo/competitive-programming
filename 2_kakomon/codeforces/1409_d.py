t=int(input())
for _ in range(t):
    n,s = map(int, input().split())

    # print('---',n)
    nsum = 0
    ns = str(n)
    for ni in ns:
        nsum += int(ni)
    if nsum <= s:
        print(0)
        continue

    for i in range(19):
        p = pow(10,i+1)
        plus = p - n%p
        new_n = n + plus
        ns = str(new_n)
        # print(ns)
        nsum = 0
        for ni in ns:
            nsum += int(ni)
        if nsum <= s:
            print(plus)
            break
