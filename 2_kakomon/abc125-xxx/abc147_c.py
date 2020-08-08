from itertools import product

n = int(input())
al = []

for _ in range(n):
    curr_al = []
    a = int(input())
    for i in range(a):
        x,y = map(int, input().split())
        curr_al.append((x,y))
    al.append(curr_al)


pattern = 2
ite = product(range(pattern),repeat=n)
ans = 0
for it in ite:
    a_01_l = list(it)
    curr_ans = a_01_l.count(1)
    # print('-----')
    # print(a_01_l)
    for i, curr_it in enumerate(it):
        if curr_it == 1:
            check = True
            for a in al[i]:
                if a_01_l[a[0]-1] != a[1]:
                    check = False
            if not check:
                break
    else:
        # print('ok')
        ans = max(curr_ans,ans)

print(ans)
