s=input()
if s[0]=='x':
    s=s[1:]
if len(s)>0 and s[0] == 'x':
    s=s[1:]

for i in range(len(s)):
    if i%3==0 and s[i]=='x':
        print('No')
        exit()
    if i%3!=0 and s[i]=='o':
        print('No')
        exit()

print('Yes')