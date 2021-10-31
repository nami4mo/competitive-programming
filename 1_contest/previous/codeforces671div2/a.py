ansl = []
for _ in range(int(input())):
    n = int(input())
    s = input()

    if n==1:
        if int(s)%2 == 0:
            ansl.append(2)
        else:
            ansl.append(1)
    elif n == 2:
        if int(s[1])%2 == 0:
            ansl.append(2)
        else:
            ansl.append(1)
    
    elif n%2 == 1:
        cnt = 0
        for i in range(0,n,2):
            if int(s[i])%2 == 1:
                cnt += 1
        if cnt >= 1:
            ansl.append(1)
        else:
            ansl.append(2)
    else:
        cnt = 0
        for i in range(1,n,2):
            if int(s[i])%2 == 0:
                cnt += 1
        if cnt >= 1:
            ansl.append(2)
        else:
            ansl.append(1)


for ans in ansl:print(ans)
