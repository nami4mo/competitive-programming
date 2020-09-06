t=int(input())
for _ in range(t):
    n = int(input())
    al = list(map(int, input().split()))
    s_al = al[:]
    s_al.sort()
    for i,a in enumerate(al):
        if a%s_al[0] != 0:
            if s_al[i] != a:
                print('NO')
                break
    else:
        print('YES')