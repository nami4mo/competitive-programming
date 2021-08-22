x = int(input())
if x == 2: 
    print(2)
    exit()
while True:
    for i in range(2, int(-(-x**0.5//1))+1):
        if x%i == 0:
            break
    else:
        print(x)
        break
    x+=1