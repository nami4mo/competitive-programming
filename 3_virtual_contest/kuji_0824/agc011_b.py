n=int(input())
al=list(map(int, input().split()))  

al.sort()
curr_ans = 1
curr_sum = al[0]
for a in al[1:]:
    if curr_sum*2 >= a:
        curr_ans += 1
        curr_sum += a
    else:
        curr_ans = 1
        curr_sum += a

print(curr_ans)