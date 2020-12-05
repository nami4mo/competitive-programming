from collections import Counter
n=int(input())
al=list(map(int, input().split()))
c=Counter(al)
tops=c.most_common(n)
tops.sort(key=lambda x: -x[0])
# if len(tops) < 2:
#     print(0)
#     exit()


# print(tops)
ans = 1
ok_cnt = 0
for l,cnt in tops:
    if cnt>=2:
        ans *= l
        ok_cnt += 1
    if ok_cnt == 2:break
    if cnt>=4:
        ans *= l
        ok_cnt += 1
    if ok_cnt == 2:break


if ok_cnt == 2:
    print(ans)
else:
    print(0)