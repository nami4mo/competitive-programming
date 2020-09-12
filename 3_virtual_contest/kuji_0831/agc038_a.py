h,w,a,b = map(int, input().split())

ansl = [[-1]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if i < b and j < a:
            ansl[i][j] = '0'
        elif i >= b and j >= a:
            ansl[i][j] = '0'
        else:
            ansl[i][j] = '1'

for a in ansl:
    print(''.join(a))

