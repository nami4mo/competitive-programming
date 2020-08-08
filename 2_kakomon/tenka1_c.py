n = int(input())
al = []

for _ in range(n):
    al.append(int(input()))


al.sort()

ans = 0
if n%2 == 0:
    mid = n//2
    curr_num = al[mid]
    curr_ans = 0
    while True:
        if n-i == mid: 
            break
        curr_ans += abs(curr_num-al[n-i])
        curr_ans += abs(al[i-1] - al[i])
        curr_num = al[i]
    ans = max(curr_ans,ans)

    curr_num = al[mid]
    curr_ans = 0
    while True:
        if i == mid: 
            break
        curr_ans += abs(curr_num-al[i])
        curr_ans += abs(al[i] - al[n-i])
        curr_num = al[n-i]
    ans = max(curr_ans,ans)