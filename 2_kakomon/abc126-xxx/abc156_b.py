n,k = map(int, input().split())
for i in range(50):
    if n < pow(k,i):
        print(i)
        exit()