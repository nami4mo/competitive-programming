import math
s=int(input())
thre = math.ceil(s**0.5)
left = thre**2
rem = left - s
for i in range(1,10**7):
    if rem%i == 0:
        a,b = i,rem//i
        break
print(0,0,thre,b,a,thre)