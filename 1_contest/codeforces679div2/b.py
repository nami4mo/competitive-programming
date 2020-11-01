import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int, input().split())
    rows = []
    for i in range(n):
        row = list(map(int, input().split()))
        rows.append(row)

    num_to_row = [-1]*(n*m+1)
    for i in range(m):
        col = list(map(int, input().split()))
        for j in range(n):
            num_to_row[col[j]] = j

    ansl = [[]]*n
    for row in rows:
        r = num_to_row[row[0]]
        ansl[r] = row

    for row in ansl:
        print(*row)