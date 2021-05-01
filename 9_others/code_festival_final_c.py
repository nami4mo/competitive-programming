a=int(input())
for i in range(10,10**6):
    s=str(i)
    v=0
    for j in range(len(s)):
        v+=int(s[j])*pow(i,len(s)-1-j)
    if v==a:
        print(i)
        exit()
    if v>a:
        print(-1)
        exit()