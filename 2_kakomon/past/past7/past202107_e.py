n=int(input())
for i in range(30):
    x=1
    for j in range(30):
        x*=3
        if i==j:x+=1
    if n==x:
        print(i+1)
        exit()
print(-1)