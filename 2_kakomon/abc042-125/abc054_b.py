n, m = map(int, input().split())
al = []
bl = []

for _ in range(n):
    row = list(input())
    al.append(row)

for _ in range(m):
    row = list(input())
    bl.append(row)

for i in range(0,n-m+1):
    for j in range(0,n-m+1):
        ok_flag = True
        for y in range(0,m):
            for x in range(0,m):
                if al[i+y][j+x] != bl[y][x]:
                    ok_flag = False
        if ok_flag:
            print('Yes')
            exit()
else:
    print('No')