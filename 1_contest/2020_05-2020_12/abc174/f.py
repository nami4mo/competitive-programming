n,q = map(int, input().split())
cl = list(map(int, input().split()))
num_set = set()
curr_same_cnt = 0
same_cnts = [0]*n

for i,c in enumerate(cl):
    if c in num_set:
        curr_same_cnt += 1
    num_set.add(c)
    same_cnts[i] = curr_same_cnt

