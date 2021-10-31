n=int(input())
dl=[]
# sums=0
aoki=0
for _ in range(n):
    a,b=map(int, input().split())
    d=2*a+b
    dl.append((d,a,b))
    aoki+=a
    # sums+=d

# sums=sum(dl)
# half=sums//2+1
# print(half,'--')
dl.sort(reverse=True)

tak=0
for i in range(n):
    d,a,b=dl[i]
    aoki-=a
    tak+=(a+b)
    # print('--',aoki,tak)
    if tak>aoki:
        print(i+1)
        exit()