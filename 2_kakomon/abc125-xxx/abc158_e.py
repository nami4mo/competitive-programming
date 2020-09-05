n,p = map(int, input().split())
s = input()

if p%2 == 0:
    ans = 0
    for i, si in enumerate(s):
        if int(si)%2 == 0:
            ans += (i+1)
    print(ans)
    exit()

if p%5 == 0:
    ans = 0
    for i, si in enumerate(s):
        if int(si)%5 == 0:
            ans += (i+1)
    print(ans)
    exit()


prem = [0]*p
prem[0] = 1
curr_rem = 0
ans = 0
s = s[::-1]
for i,si in enumerate(s):
    sii = int(si)
    curr_rem = (sii*pow(10,i,p)+curr_rem)%p
    ans += prem[curr_rem]
    prem[curr_rem] += 1

print(ans)
    