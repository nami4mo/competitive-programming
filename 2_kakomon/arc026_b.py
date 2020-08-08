n = int(input())

if n <= 2:
    print('Deficient')
    exit()

div_sum = 0
for i in range(1, int(n**0.5)+1):
    if i*i > n: break
    if n%i == 0:
        div_sum += i
        if i*i != n and i != 1:
            div_sum += n//i

if div_sum < n:
    print('Deficient')
elif div_sum == n:
    print('Perfect')
else:
    print('Abundant')