a, b = map(float, input().split()) 
a = int(a)
b*=100
b = int(round(b))
# print(a,b)
ans = a*b
ans = ans//100
print(ans)

# import math
# print(0.11*100)
# i = 0.01
# while i <= 1.00:
#     print(round(i*100))
#     i+=0.01