n=int(input())  
ans = 0
for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        # print('----',i)
        a = i
        x1 = n//i
        x = x1-1
        # print(a,x)
        if a < x:
            ans += x
        
        a = n//i
        x1 = i
        x = x1 - 1
        if a < x:
            ans += x

print(ans)