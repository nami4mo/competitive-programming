h = int(input())
d = 0
for i in range(1000):
    if pow(2,i) <= h < pow(2,i+1):
        d = i+1
        break

print(pow(2,d)-1)