alps = 'abcdefghijklmnopqrstuvwxyz' # string.ascii_lowercase
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # string.ascii_uppercase

s=input()
ans=True
for i in range(len(s)):
    if i%2==0 and s[i] in ALPS: ans=False
    if i%2==1 and s[i] in alps: ans=False

if ans:print('Yes')
else:print('No')