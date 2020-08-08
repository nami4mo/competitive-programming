# from functools import lru_cache

# @lru_cache
# def com(n,r):
#     v = 1
#     for i in range(1,n+1): v*=i
#     for i in range(1,r+1): v=v//i
#     for i in range(1,n-r+1): v=v//i
#     return v

def com(n,r):
    v = 1
    for i in range(n+1-r,n+1): v*=i
    for i in range(1,r+1): v=v//i
    return v
    


n,d = map(int, input().split())
x,y = map(int, input().split())

if x%d != 0 or y%d != 0:
    print(0.0)
    exit()

need_x = abs(x)//d
need_y = abs(y)//d


# print(need_x,need_y)
ans = 0
comb = 0
for x_cnt in range(n+1):
    y_cnt = n-x_cnt
    if need_x > x_cnt or need_y > y_cnt:
        # print(x_cnt,'a')
        continue

    if (x_cnt+need_x)%2 != 0 or (y_cnt+need_y)%2 != 0:
        # print(x_cnt)
        continue

    x_num = (x_cnt+need_x)//2
    y_num = (y_cnt+need_y)//2

    val = com(x_cnt,x_num)*com(y_cnt,y_num)*com(n,x_cnt)

    # probx = com(x_cnt,x_num)/pow(2,x_cnt)
    # proby = com(y_cnt,y_num)/pow(2,y_cnt)
    # allprob = com(n,x_cnt)/pow(2,n)
    # val = probx*proby*allprob
    comb += val

print(comb/pow(2,2*n))