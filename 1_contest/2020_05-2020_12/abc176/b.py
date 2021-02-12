n = input()  
val = 0
for ni in n:
    val += int(ni)

if val%9 == 0:
    print('Yes')
else:
    print('No')