for _ in range(int(input())):
    n=int(input())
    al=list(map(int, input().split()))
    if n%2==0:
        print('YES')
    else:
        for i in range(n-1):
            if al[i] >= al[i+1]:
                print('YES')
                break
        else:
            print('NO')