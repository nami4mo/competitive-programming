from itertools import combinations


n,m = map(int, input().split())
xyl = [[False]*n for _ in range(n)]
for _ in range(m):
    x,y = map(int, input().split())
    x-=1
    y-=1
    xyl[x][y] = True
    xyl[y][x] = True

ll = list(range(n))  # list of elements

for i in range(n,0,-1):
    combl = list(combinations(ll, i))
    # print(combl)
    for comb in combl:
        break_flag = False
        curr_l = list(comb)
        for j in range(i):
            for k in range(j+1,i):
                if not xyl[curr_l[j]][curr_l[k]]:
                    break_flag = True
                    break
            if break_flag:
                break
        else:
            print(i)
            exit()