n=int(input())
for i in range(0,100):
    if pow(2,i)>n:
        print(i-1)
        exit()