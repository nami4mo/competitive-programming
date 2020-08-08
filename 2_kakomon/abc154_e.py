n = input()
k = int(input())
keta = len(n)


dp_small = [ [0]*5 for _ in range(keta+1)]
dp_same = [ [0]*5 for _ in range(keta+1)]

dp_small[0][0] = 0
dp_same[0][0] = 1

for i in range(keta):
    num = int(n[i])
    for j in range(4):
        dp_small[i+1][j+1] += dp_small[i][j] * 9
        dp_small[i+1][j] += dp_small[i][j]
        if num != 0:
            dp_small[i+1][j+1] += dp_same[i][j]*(num-1)
            dp_small[i+1][j] += dp_same[i][j]

        if num == 0:
            dp_same[i+1][j] += dp_same[i][j]
        else:
            dp_same[i+1][j+1] += dp_same[i][j]

print(dp_same[-1][k]+dp_small[-1][k])