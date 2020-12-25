s_orig=list(input())
alps = 'abcdefghijklmnopqrstuvwxyz'
ans = 10**5
for alp in alps:
    if alp not in s_orig:continue
    if all([si == alp for si in s_orig]):
        print(0)
        exit()
    s = s_orig[:]
    while True:
        new_s = []
        ok_flag = True
        for i in range(len(s)-1):
            if alp == s[i] or alp == s[i+1]:
                new_s.append(alp)
            else:
                new_s.append('.')
                ok_flag = False
        if ok_flag:
            ans = min(ans, len(s_orig)-len(new_s))
            break
        s = new_s[:]

print(ans)