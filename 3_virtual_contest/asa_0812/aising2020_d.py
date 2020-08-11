n = int(input())
xs = input()
x = int(xs, 2)

ansl = [0]*n
for i in range(1,n):
    ans = 0
    num = i
    while True:
        pc = bin(num).count("1")
        num %= pc
        ans += 1
        if num == 0: break
    ansl[i] = ans

pc = bin(x).count("1")
if pc == 0:
    for i in range(n):
        print(1)
        exit()


next_num = x%pc
next_num_p1 = x%(pc+1)
if pc != 1:
    next_num_m1 = x%(pc-1)
else:
    next_num_m1 = None

for i in range(n):
    bit = (1<<(n-1-i))
    if xs[i] == '0':
        num = (next_num_p1 + pow(2,n-1-i,pc+1)) % (pc+1)
        ans = ansl[num] + 1
    else:
        if pc != 1:
            num = (next_num_m1 - pow(2,n-1-i,pc-1)) % (pc-1)
            ans = ansl[num] + 1
        else:
            ans = 0
    print(ans)