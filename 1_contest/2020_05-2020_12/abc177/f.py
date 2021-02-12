h,w = map(int, input().split())
abl = []

ansl = []
curr_w = 1
curr_ans = 0
for _ in range(h):
    a,b = map(int, input().split())
    if curr_w < a:
        curr_ans += 1
    elif: a <= curr_w < b:
        curr_ans += (b+1-curr_w)
        curr_ans += 1
        curr_w = b+1
    else:
        curr_ans
