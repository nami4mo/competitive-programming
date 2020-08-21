n = int(input())    
xl = list(map(int, input().split()))   
ans = 10**10 
for i in range(1,101):
    v = 0
    for x in xl:
        v += (x-i)**2
    ans = min(ans,v)

print(ans)