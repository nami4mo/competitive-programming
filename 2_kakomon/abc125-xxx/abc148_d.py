n = int(input())
a_list = list(map(int, input().split())) 

break_cnt = 0
next_num = 1
for a in a_list:
    if a == next_num:
        next_num +=1
    else:
        break_cnt+=1

if break_cnt != n:
    print(break_cnt)
else:
    print(-1)