s = list(input())

s_set = set()
s_set.add('.')
if len(s) >= 2:
    s_set.add('..')
if len(s) >= 3:
    s_set.add('...')

for i in range(len(s)):
    s_set.add(s[i])
    if i != 0:
        s_set.add('.'+s[i])
    if i != len(s)-1:
        s_set.add(s[i]+'.')
        s_set.add(s[i]+s[i+1])
    if i >=2:
        s_set.add('..'+s[i])
        s_set.add('.'+s[i-1]+s[i])
    if i <= len(s)-3:
        s_set.add(s[i]+'..')
        s_set.add(s[i]+s[i+1]+s[i+2])
        s_set.add(s[i]+s[i+1]+'.')
        s_set.add(s[i]+'.'+s[i+2])
    if i != 0 and  i != len(s)-1:
        s_set.add('.'+s[i]+'.')

print(len(s_set))
# print(s_set)