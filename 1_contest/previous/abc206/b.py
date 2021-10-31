n=int(input())
for i in range(1,10**8):
    v=i*(i+1)//2
    if v>=n:
        print(i)
        exit()