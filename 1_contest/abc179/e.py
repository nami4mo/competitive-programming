n,x,m = map(int, input().split())

ans = 0
f = [-1]*m # a->f
f[x] = 0

ansl = [x]
curr_x = x
loop_start = -1
for i in range(n-1):
    cnt = i+1
    x2 = (curr_x**2)%m
    if f[x2] == -1:
        ansl.append(x2)
        f[x2] = cnt
    else:
        loop_start = f[x2]
        break
    curr_x = x2
else:
    print(sum(ansl))
    exit()

amari = ansl[0:loop_start]

n_rem = n - loop_start
loop_l = ansl[loop_start:]
loop_len =len(loop_l)
loop_sum = sum(loop_l)

loop_cnt = n_rem//loop_len
loop_amari = n_rem - loop_cnt*loop_len

ans = sum(amari) + sum(loop_l)*loop_cnt + sum(loop_l[:loop_amari])
print(ans)