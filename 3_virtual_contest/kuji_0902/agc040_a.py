s = input()
s += 'a'
cnts = []
prev = s[0]
cnt = 1
for i,si in enumerate(s[1:]):
    if prev == si:
        cnt += 1
    else:
        cnts.append(cnt)
        cnt = 1
    prev = si


ans = 0
c_num = 0
if s[0] == '<':
    for i,c in enumerate(cnts):
        if i%2 == 0:
            ans += c*(c-1)//2
            c_num = c-1
        else:
            ans += c*(c-1)//2
            ans += max(c,c_num+1)
    if s[-2] == '<':
        ans += cnts[-1]
        # print(cnts[-1])
    print(ans)

if s[0] == '>':
    ans = cnts[0]*(cnts[0]+1)//2
    for i,c in enumerate(cnts[1:]):
        if i%2 == 0:
            ans += c*(c-1)//2
            c_num = c-1
        else:
            ans += c*(c-1)//2
            ans += max(c,c_num+1)
        
    if s[-2] == '<':
        ans += cnts[-1]
    print(ans)

# print(cnts)