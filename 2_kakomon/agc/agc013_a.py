n = int(input())
al = list(map(int, input().split()))

flag = 0
ans = 1
for i in range(n-1):
    if al[i] > al[i+1]:
        if flag == 1:
            ans += 1
            flag = 0
        else:
            flag = -1
    elif al[i] == al[i+1]:
        pass
    else:
        if al[i] < al[i+1]:
            if flag == -1:
                ans += 1
                flag = 0
            else:
                flag = 1

print(ans)