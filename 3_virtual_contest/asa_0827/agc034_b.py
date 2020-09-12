s = input()
s = s.replace('BC','x')

a_flag = False
ans = 0
last_a = 0
for si in s:
    if si == 'A':
        a_flag = True
        last_a += 1
    elif si == 'x' and a_flag:
        ans += last_a
    else:
        a_flag = False
        last_a = 0

print(ans)
