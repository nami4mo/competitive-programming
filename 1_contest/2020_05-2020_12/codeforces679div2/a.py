for _ in range(int(input())):
    n = int(input())
    al = list(map(int, input().split()))
    ansl = []
    for i in range(n//2):
        ansl.append(al[i*2+1])
        ansl.append(-al[i*2])
    print(*ansl)