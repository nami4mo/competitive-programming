n,m = map(int, input().split())
bl = []
for _ in range(n):
    row = list(map(int, list(input())))
    bl.append(row)

ans = [ [0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        # if (i,j) in [ (0,m-1), (0,0), (n-1,0), (n-1,m-1)]:
        #     continue
        if i == 0 or i == n-1 or j == 0 or j == m-1:
            continue
        top = ans[i-2][j]
        left = ans[i-1][j-1]
        right = ans[i-1][j+1]
        ans[i][j] = bl[i-1][j] - top - left - right

for a in ans:
    row = list(map(str,a))
    row = ''.join(row)
    print(row)