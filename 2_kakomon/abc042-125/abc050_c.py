n = int(input())
al = list(map(int, input().split()))

# 4... 1,3
# 6... 1,3,5
if n%2 == 0:
    cnts = [0]*n
    for a in al:
        if a >= n:
            print('0')
            exit()
        cnts[a] += 1
    for i,c in enumerate(cnts):
        if i%2 == 0 and c != 0:
            print(0)
            exit()
        if i%2 == 1 and c!= 2:
            print(0)
            exit()
    ans = pow(2,n//2,10**9+7)
    print(ans)

# 5... 0=1, 2,4 = 2
else:
    cnts = [0]*n
    for a in al:
        if a >= n:
            print('0')
            exit()
        cnts[a] += 1
    for i,c in enumerate(cnts):
        if i == 0 and c != 1:
            print(0)
            exit()        
        elif i%2 == 1 and c != 0:
            print(0)
            exit()
        elif i%2 == 0 and i > 0 and c!= 2:
            print(0)
            exit()
    ans = pow(2,n//2,10**9+7)
    print(ans)