x,y = map(int, input().split())

for i in range(x+1):
    a = i
    b = x - i
    ashi = 2*a + 4*b
    if ashi == y: 
        print('Yes')
        break
else:
    print('No')