N, K = map(int, input().split()) 
dl = list(map(str, input().split())) 

curr_num = N
while True:
    n_str = str(curr_num)
    for d in dl:
        if d in n_str:
            curr_num += 1
            break
    else:
        print(curr_num)
        break