cl = [list(input().split()) for _ in range(4)]
# print(cl)

for i in range(3,-1,-1):
    for j in range(3,-1,-1):
        print(cl[i][j]+' ', end='')
    print()