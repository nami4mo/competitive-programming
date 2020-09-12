n = int(input())
vl = list(map(int, input().split()))

zero_d = {}
one_d = {}
for i,v in enumerate(vl):
    if i%2 == 0:
        zero_d.setdefault(v,0)
        zero_d[v] += 1
    else:
        one_d.setdefault(v,0)
        one_d[v] += 1

zero_l = sorted(zero_d.items(), reverse=True, key=lambda x:x[1])
one_l = sorted(one_d.items(), reverse=True, key=lambda x:x[1])


zero_l.append((-1,0))
one_l.append((-1,0))

zero_cnt = (n+1)//2
one_cnt = n//2
if zero_l[0][0] != one_l[0][0]:
    ans = n - zero_l[0][1] - one_l[0][1]
else:
    ans1 = n - zero_l[0][1] - one_l[1][1]
    ans2 = n - zero_l[1][1] - one_l[0][1]
    ans = min(ans1,ans2)

print(ans)