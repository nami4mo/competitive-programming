n = int(input())

if n == 2:
    print('Takahashi')
    exit()

flag = True
first = True
l = n
r = n
while True:
    if flag:
        if first:
            l,r = l//2+1, l-1
            first = False
        else:
            l,r = (l+1)//2, l-1
    else:
        l,r = l//2, l-1
    flag = not flag
    # print(flag, l, r)
    if l <= 1 or r <= 1:
    # if l <= 1:
        break

if flag:
    print('Takahashi')
else:
    print('Aoki')