import math
a, b, n = map(int, input().split()) 

ans = 0
if n < b:
    ans = math.floor(a*n/b) 
else:
    ans = math.floor(a*(b-1)/b) 

print(ans)