s = input()
t = input()

s_d = {}
t_d = {}
for i in range(len(s)):
    if s[i] not in s_d:
        new_num = len(s_d)+1
        s_d[s[i]] = new_num
        s_valid = -1
    else:
        s_valid = s_d[s[i]]

    if t[i] not in t_d:
        new_num = len(t_d)+1
        t_d[t[i]] = new_num
        t_valid = -1
    else:
        t_valid = t_d[t[i]]

    if s_valid != t_valid:
        print('No')
        break

else:
    print('Yes')