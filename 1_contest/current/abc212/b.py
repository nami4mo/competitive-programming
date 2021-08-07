x=input()
for i in range(3):
    if x[i]!=x[i+1]:break
else:
    print('Weak')
    exit()

for i in range(3):
    # print(int(x[i]),(int(x[i+1])+1)%10)
    if (int(x[i])+1)%10!=(int(x[i+1]))%10:break
else:
    print('Weak')
    exit()

print('Strong')