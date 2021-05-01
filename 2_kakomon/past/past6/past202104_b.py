b=input()
b=b.replace('past','x')
b=b.replace('post','y')
for i in range(len(b)):
    if b[i]=='y':
        print(i+1)
        break
else:
    print('none')