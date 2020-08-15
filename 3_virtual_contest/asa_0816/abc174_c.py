k = int(input())
rem = 7%k
for i in range(10**6+1):
    if rem == 0:
        print(i+1)
        break
    rem = (rem*10+7)%k
else:
    print(-1)