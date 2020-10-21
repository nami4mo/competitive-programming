a,b = map(int, input().split())

cl1 = [ ['#']*100 for _ in range(50)]
cl2 = [ ['.']*100 for _ in range(50)]

h = 0
w = 0
for i in range(a-1):
    cl1[h][w] = '.'
    w += 2
    if w >= 100:
        h+=2
        # w = (w+1)%2
        w = 0

h = 1
w = 0
for i in range(b-1):
    cl2[h][w] = '#'
    w += 2
    if w >= 100:
        h+=2
        # w = (w+1)%2
        w = 0


print(100,100)
for row in cl1:
    print(''.join(row))

for row in cl2:
    print(''.join(row))