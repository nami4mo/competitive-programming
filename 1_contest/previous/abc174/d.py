
n = int(input())
cl = list(input())

ans = 0
front = 0
back = n-1
while True:

    detected_w = 999999999
    for i in range(front,n):
        if cl[i] == 'W':
            detected_w = i
            break
    else:
        print(ans)
        exit()

    detected_r = -1
    for i in range(back,-1,-1):
        if cl[i] == 'R':
            detected_r = i
            break
    else:
        print(ans)
        exit()

    # print(detected_w, detected_r)
    if detected_w < detected_r:
        ans += 1
        front = detected_w+1
        back = detected_r-1
    else:
        print(ans)
        exit()

