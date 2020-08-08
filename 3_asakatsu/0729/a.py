al = list(map(int, input().split()))
al.sort()
if al[0] == 5 and al[1] == 5 and al[2] == 7:
    print('YES')
else:
    print('NO')