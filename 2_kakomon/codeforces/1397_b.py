n = int(input())
al = list(map(int, input().split()))
if n > 50:
    ans = 0
    for a in al:
        ans += abs(a-1)
    print(ans)
    exit()


ans = 0
for a in al:
    ans += abs(a-1)
al.sort()
c = 2
while True:
    cp = 1
    curr_ans = 0
    for i,a in enumerate(al):
        curr_ans += abs(a-cp)
        cp *= c
    if ans < curr_ans:
        print(ans)
        exit()
    else:
        ans = curr_ans
        c += 1