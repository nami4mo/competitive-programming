from itertools import product

n = int(input())
n_len = len(str(n))
ans = 0
for i in range(3,n_len):
    ite = product(range(3),repeat=i)
    for it in ite:
        if 0 in it and 1 in it and 2 in it:
            ans += 1


num_d = {0:7,1:5,2:3}
ite = product(range(3),repeat=n_len)
for it in ite:
    if 0 in it and 1 in it and 2 in it:
        curr_num = 0
        for i,j in enumerate(it):
            curr_num += num_d[j]*(10**(n_len-1-i))
        if curr_num <= n: 
            ans+=1

print(ans)