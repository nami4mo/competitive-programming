a,b = input().split()
s = a+b
v = int(s)

for i in range(1,1000):
    if v == i*i: 
        print('Yes')
        break
else:
    print('No')