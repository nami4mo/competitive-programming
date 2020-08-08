n,q = map(int, input().split())
s = input()

ac_cnts = [0]*(n)
curr_cnt = 0
for i, (s1,s2) in enumerate(zip(s[:-1],s[1:])):
    if s1 == 'A' and s2 == 'C':
        curr_cnt += 1
    ac_cnts[i+1] = curr_cnt

ans = []
for _ in range(q):
    l,r = map(int, input().split())
    l-=1
    r-=1
    ans.append(ac_cnts[r]-ac_cnts[l])

# print(ac_cnts)
# print(ans)

for a in ans:
    print(a)