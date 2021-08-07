n=input()
for i in range(11):
    nn='0'*i+n
    if nn==nn[::-1]:
        print('Yes')
        exit()
print('No')