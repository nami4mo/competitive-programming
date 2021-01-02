x,y = map(int, input().split())
if y == 0:
    print('ERROR')
    exit()

x *= 100
ans = x//y/100
print('{:.2f}'.format(ans))
