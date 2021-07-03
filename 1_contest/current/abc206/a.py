n=int(input())
v=n*1.08
v=int(v)
if v<206:
    print('Yay!')
elif v==206:
    print('so-so')
else:
    print(':(')