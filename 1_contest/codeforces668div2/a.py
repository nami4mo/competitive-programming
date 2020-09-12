for _ in range(int(input())):
    n = int(input())
    al = list(map(int, input().split()))
    ans = al[::-1]
    print(*ans)