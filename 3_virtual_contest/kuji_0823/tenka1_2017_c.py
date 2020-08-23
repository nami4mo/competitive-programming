N = int(input())    

for h in range(1,3501):
    for n in range(h,3501):
        top = N*h*n
        bottom = 4*h*n-N*n-N*h
        if bottom > 0 and top%bottom == 0:
            print(h,n,top//bottom)
            exit()
