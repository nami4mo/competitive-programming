
n = int(input())
bl = list(map(int, input().split()))

curr_bl = bl[:]

ans = []
for i in range(n):
    rem = n - i
    deleted_j = -1
    for j in range(rem-1,-1,-1):
        if curr_bl[j] == j+1:
            deleted_j = j
            ans.append(j+1)
            break
    if deleted_j == -1:
        print(-1)
        exit()
    else:
        new_bl = []
        for j in range(rem):
            if j != deleted_j:
                new_bl.append(curr_bl[j])
        curr_bl = new_bl[:]


for a in ans[::-1]:
    print(a)