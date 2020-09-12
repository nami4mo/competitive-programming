n,m = map(int, input().split())
al = list(map(int, input().split()))

cnts = [0]*(m+1)
good = -1
for a in al:
    cnts[a] += 1
    if cnts[a] >= n//2 + 1:
        if good != -1 and good != a:
            print('?')
            exit()
        good = a

if good == -1:
    print('?')
    exit()
print(good)