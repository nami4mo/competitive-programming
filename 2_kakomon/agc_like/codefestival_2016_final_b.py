n=int(input())
maxn=0
nsum=0
for i in range(10**5):
    v = i*(i+1)//2
    if v>=n:
        maxn=i
        rem=v-n
        for j in range(1,maxn+1):
            if j==rem:continue
            print(j)
        exit()