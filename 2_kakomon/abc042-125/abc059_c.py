
n = int(input())
al = list(map(int, input().split())) 


ans1 = 0
curr_sum = 0
next_sign = 1
for a in al:
    next_sum = curr_sum + a
    if next_sum >= 0 and next_sign == -1: 
        ans1 += next_sum+1
        next_sum = -1
    elif next_sum <= 0 and next_sign == 1:
        ans1 += (1-next_sum)
        next_sum = 1
    curr_sum = next_sum
    next_sign *= -1


ans2 = 0
curr_sum = 0
next_sign = -1
for a in al:
    next_sum = curr_sum + a
    if next_sum >= 0 and next_sign == -1: 
        ans2 += next_sum+1
        next_sum = -1
    elif next_sum <= 0 and next_sign == 1:
        ans2 += (1-next_sum)
        next_sum = 1
    curr_sum = next_sum
    next_sign *= -1

print(min(ans1,ans2))