for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    elif n == 3:
        print(2)
    elif n%2 == 0:
        print(2)
    else:
        print(3)

    # for i in range(2,int(n**0.5)+1):
    #     if n%i == 0:
    #         print(i)
    #         break
    # else:
    #     print(n-1)
